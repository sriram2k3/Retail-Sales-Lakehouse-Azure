import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv

DB_HOST = os.environ.get("DATABASE_HOST", "localhost")  # Defaults to 'localhost' if missing
DB_USER = os.environ.get("DATABASE_USER")
DB_PASSWORD = os.environ.get("DATABASE_PASSWORD")
DB_NAME = os.environ.get("DATABASE_NAME")

conn = mysql.connector.connect(
    host = DB_HOST,
    user= DB_USER,
    password= DB_PASSWORD,
    database= DB_NAME
)

if conn:
    print("Connected")
    conn.close()
    print("Connection closed")
else:
    print("Not connected")