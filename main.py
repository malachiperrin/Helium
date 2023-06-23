import sys
import os
import shutil
from pathlib import Path
import time

from rich import print as rich_print
from rich.console import Console
from rich.table import Table
import dotenv


from database.database_setup import setup


dotenv.load_dotenv()


def set_path():
    confirm_path = '2'

    while confirm_path != '1': 
        file_path = input("please enter the file path\nEnter 3 to select from a list of files in the csv directory\n>> ")

        if(file_path == '3') :
            csv_dir = Path("csv/")
            for csv_file in csv_dir.iterdir():
                print(format(csv_file.name))
                
            file_name = input("To select, enter name associated with file\n>> ")
            file_path = os.getcwd() + "/csv/{}".format(file_name)
        

        rich_print("[bold green]{}[/bold green]".format(file_path))    
        confirm_path = input("Is the path correct?\nYes = 1\nNo = 2\n>> ")

    # Files get copied to the CSV directory for organization

    file_name = os.path.basename(file_path);

    return file_name




def main() : 
    rich_print("Welcome to [bold blue]Helium![/bold blue]")
    

    file_name = set_path();




    if(os.path.exists("csv/" + file_name)) :
        print("\nThis file already exists in the csv directory")
        time.sleep(3)
    elif(not os.path.exists(os.getcwd() + "/csv")):
        os.makedirs(os.getcwd() + "/csv")
        shutil.copy(file_path, os.getcwd() + "/csv")
    else :
        shutil.copy(file_path, os.getcwd() + "/csv")

    data = []

    with open("csv/{}".format(file_name), 'r', encoding='unicode_escape') as file:
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


    setup(str(os.getenv("DATABASE_DRIVER")))


    
main()
