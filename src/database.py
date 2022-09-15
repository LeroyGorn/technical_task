from sqlalchemy import MetaData, Table, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import sqlalchemy as db
from .models import Ads


Base = declarative_base()
table_objects = [Ads.__table__]


class Database():
    engine = db.create_engine('postgresql://admin:secret@host.docker.internal/parse_db')

    def __init__(self):
        self.connection = self.engine.connect()

    def saveData(self, ads):
        session = Session(bind=self.connection)
        session.add(ads)
        session.commit()

    def fetchAdByTitle(self):
        meta = MetaData()
        ads = Table('ads', meta,
                    Column('img'),
                    Column('title'),
                    Column('date'),
                    Column('location'),
                    Column('bedrooms'),
                    Column('description'),
                    Column('price'),
                    Column('currency'))
        data = self.connection.execute(ads.select())
        for ad in data:
            print(ad)

    def fetchAllAds(self):
        self.session = Session(bind=self.connection)
        ads = self.session.query(Ads).all()
        for ad in ads:
            print(ad)

    def fetchByQyery(self, query):
        fetchQuery = self.connection.execute(f"SELECT * FROM {query}")

        for data in fetchQuery.fetchall():
            print(data)

    def deleteAds(self, ads):
        session = Session(bind=self.connection)
        ad = session.query(Ads).filter(Ads.title==ads).first()
        session.delete(ad)
        session.commit()
