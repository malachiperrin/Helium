import sqlite3

def sqliteconnect(host) :

    try: 
        connection = sqlite3.connect(host)
        cursor = connection.cursor()
    except sqlite3.DatabaseError as err:
        print(err)

