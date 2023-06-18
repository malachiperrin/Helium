from database.db_mysql import mysqlconnect
from database.db_postgresql import postgresqlconnect
from database.db_sqlite import sqliteconnect

def setup(driver) :
    confirm_update = input("Are you ready to proceed with the update?\nYes = 1\nNo = 2\n>> ")

    if(confirm_update == "1") :
        if (driver == "MYSQL") :
            mysqlconnect()
        elif (driver == "SQLITE") :
            sqliteconnect()
        elif(driver == "POSTGRESQL") :
            postgresqlconnect()
        else :
            print("Please check your database driver in the .env file")
    else:
        print("when you re run the app you'll be able to choose to upload from a file in the csv directory")



def updatedatabasetable(data) :
    stmt = "UPDATE {} VALUES({})"


