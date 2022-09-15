from __future__ import print_function
import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()

database = {
    "NAME": os.getenv("POSTGRES_DB"),
    "USER": os.getenv("POSTGRES_USER"),
    "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
    "HOST": os.getenv("POSTGRES_HOST"),
    "PORT": os.getenv("POSTGRES_PORT"),
}

myConnection = psycopg2.connect(
    host=database.get("HOST"),
    user=database.get("USER"),
    password=database.get("PASSWORD"),
    dbname=database.get("NAME"))

myConnection.close()
