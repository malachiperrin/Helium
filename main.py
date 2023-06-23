import sys
import os
import shutil
import time


from rich.console import Console
from rich.table import Table
import dotenv


from database.database_setup import setup


dotenv.load_dotenv()


def main() : 
    print("Welcome to Helium!")
    

    confirm_path = '2'

    while confirm_path != '1': 
        filepath = input("please enter file path: ")
        confirm_path = input("Is the path correct?\nYes = 1\nNo = 2\n>> ")

    # D:\export.csv

    # Files get copied to the CSV directory for organization

    filename = os.path.basename(filepath);

    if(os.path.exists("csv/" + filename)) :
        print("\nThis file already exists in the csv directory")
        time.sleep(3)
    elif(not os.path.exists(os.getcwd() + "/csv")):
        os.makedirs(os.getcwd() + "/csv")
        shutil.copy(filepath, os.getcwd() + "/csv")
    else :
        shutil.copy(filepath, os.getcwd() + "/csv")

    data = []

    with open("csv/{}".format(filename), 'r', encoding='unicode_escape') as file:
        for (index, line) in enumerate(file):
            # data = line.readline()

            if(index == 0) :
                columns =  line.split(',')
            else :
                data.append(line.split(','))


    table = Table(title="Data")

    for column in columns:
        table.add_column(column)

    for row in data:
        table.add_row(*row, style='bright_green')

    console = Console()
    console.print(table)


    setup(str(os.getenv("DATABASE_DRIVE")))


    
main()
