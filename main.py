import sys
import os
import shutil
import time
from rich.console import Console
from rich.table import Table

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
    else :
        shutil.copy(filepath, os.getcwd() + "/csv")

    data = []

    with open("csv/" + filename, 'r') as file:
        for (index, line) in enumerate(file):
            # data = line.readline()

            if(index == 0) :
                columns = line.split(',')
            else :
                data.append(line.split(','))


    table = Table(title="Data")

    for column in columns:
        table.add_column(column)

    for row in data:
        table.add_row(*row, style='bright_green')

    console = Console()
    console.print(table)

    confirm_update = input("Are you ready to proceed with the update?\nYes = 1\nNo = 2\n>> ")
    
main()