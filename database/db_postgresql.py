import psycopg2

def postgresqlconnect(database_name,database_user) :

    try:
        connection = psycopg2.connect(database_name, database_user)
        cursor = connection.cursor()
    except psycopg2.DatabaseError as err:
        print(err)

