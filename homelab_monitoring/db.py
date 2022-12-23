import mysql.connector
from configuration import config

def connect():
    return mysql.connector.connect(
        host = config("DB_HOST"),
        user = config("DB_USERNAME"),
        passwd = config("DB_PASSWORD"))

