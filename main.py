import sys
import os
import shutil
import time

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

    with open("csv/" + filename, 'r') as file:
        contents = file.readline()
        print(contents)

    

main()