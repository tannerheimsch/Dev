#!/usr/bin/env python3

import csv
from objects import DailySales, SalesList

ALL_SALES = "all_sales.csv"
NEW_SALES = "new_sales.csv"
IMPORTED_FILES = "imported_files.txt"

def get_all_sales():
    sales_list = []
    with open(ALL_SALES,newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row == []:
                sales_list = []
            else:
                correct_data_types(row)
                sales_list.append(row)
    return sales_list

def correct_data_types(row):
    row[0] = float(row[0])  #amount
    row[1] = int(row[1])    #month
    row[2] = int(row[2])    #day
    row[3] = int(row[3])    #year
    row[4] = int(row[4])    #quarter


def save_all_sales(sales_list):
    with open(ALL_SALES, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(sales_list)

def already_imported(filename):
    with open(IMPORTED_FILES) as file:
        files = file.readlines();
        for line in files:
            line = line.replace("\n", "") #removes newline character from each line in file.
            if line == filename:
                return True
    return False

def add_imported_file(filename):
    with open(IMPORTED_FILES,"a") as file:
        file.write(f"{filename}\n")
        
def import_sales(filename):
    sales_list = []
    print(filename)
    with open(filename, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            correct_data_types(row)
            sales_list.append(row)
    return sales_list


        
    









