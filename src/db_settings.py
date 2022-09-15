from __future__ import print_function
import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()

database = {
    "NAME": "parse_db",
    "USER": "admin",
    "PASSWORD": "secret",
    "HOST": "host.docker.internal",
    "PORT": 5432,
}

myConnection = psycopg2.connect(
    host=database.get("HOST"),
    user=database.get("USER"),
    password=database.get("PASSWORD"),
    dbname=database.get("NAME"))

myConnection.close()
