import mysql.connector
from mysql.connector import errorcode

import os
import dotenv

dotenv.load_dotenv()

def mysqlconnect() :

    try:
        cnx = mysql.connector.connect(user = os.getenv("DATABASE_USER"), password = os.getenv("DATABASE_PASSWORD"), host=os.getenv("DATABASE_HOST"), database=os.getenv("DATABASE_NAME"))
    
        cnx.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()
