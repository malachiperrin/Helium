import mysql.connector

import os
import dotenv

dotenv.load_dotenv()

def mysqlconnect() :
    cnx = mysql.connector.connect(user = os.getenv("DATABASE_USER"), password = os.getenv("DATABASE_PASSWORD"), host=os.getenv("DATABASE_HOST"), database=os.getenv("DATABASE_NAME"))

    cnx.close()