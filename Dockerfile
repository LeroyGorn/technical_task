FROM python:3.10


RUN mkdir /technical_task

WORKDIR /technical_task

COPY ./main.py ./main.py
COPY ./src ./src
COPY requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt
