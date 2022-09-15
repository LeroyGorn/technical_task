import logging
import re
import requests
import datetime
from bs4 import BeautifulSoup
from src.database import Database
from src.models import Ads


db = Database()


def parse_page(soup):
    cards = soup.find_all('div', class_='search-item')
    for card in cards:
        img = get_image_href(card.find('img'))
        title = card.find('a', class_='title').getText().strip()
        date_posted = card.find('span', class_='date-posted').getText().strip()
        date = get_date(date_posted)
        location = card.find('div', class_='location').find('span', class_='').getText().strip()
        bedrooms = card.find('span', class_='bedrooms').getText().split(':')[1].strip()
        description = get_description(card.find('div', class_='description'))
        price_text = card.find('div', class_='price').getText().strip()
        currency, price = get_price(price_text)
        item = Ads(
            image=img,
            title=title,
            date=date,
            location=location,
            bedrooms=bedrooms,
            description=description,
            price=price,
            currency=currency
        )
        db.saveData(item)


def get_price(price_text):
    if not price_text[0].isalpha():
        return price_text[0], price_text[1:]
    return None, price_text


def get_description(description_tag):
    return ''.join(description_tag.find_all(text=True, recursive=False)).strip()


def get_date(date_posted):
    if '<' in date_posted:
        hours = int(re.findall(r'\d+', date_posted)[0])
        date_posted = datetime.datetime.now() - datetime.timedelta(hours=hours)
        date_posted = datetime.datetime.strptime(str(date_posted.date()), '%Y-%m-%d')
    elif date_posted == 'Yesterday':
        date_posted = datetime.datetime.now() - datetime.timedelta(days=1)
        date_posted = datetime.datetime.strptime(str(date_posted.date()), '%Y-%m-%d')
    else:
        date_posted = datetime.datetime.strptime(str(date_posted), '%d/%m/%Y')
    return date_posted.strftime('%d-%m-%Y')


def get_image_href(img_tag):
    return img_tag.get('data-src') if 'data-src' in img_tag.attrs else img_tag.get('src')


log_format = '[%(asctime)s] [%(levelname)s] - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_format)
logger = logging.getLogger()
WEBSITE_URL = 'https://www.kijiji.ca'
page_url = '/b-apartments-condos/city-of-toronto/c37l1700273'

while page_url:
    logger.info(f'Getting {WEBSITE_URL + str(page_url)}...')
    response = requests.get(WEBSITE_URL + str(page_url))
    soup = BeautifulSoup(response.text, 'html.parser')
    parse_page(soup)
    next_button = soup.find('a', attrs={'title': 'Next'})
    page_url = next_button.get('href') if next_button else None
