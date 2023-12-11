import csv

ALL_SALES = "all_sales.csv"
NEW_SALES = "new_sales.csv"
IMPORTED_FILES = "imported_files.txt"

def get_all_sales():
    sales_list = []
    with open(ALL_SALES,newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            correct_data_types(row)
            sales_list.append(row)
    return sales_list

def correct_data_types(row):
    row[0] = float(row[0])  # amount
    row[1] = int(row[1])    # month
    row[2] = int(row[2])    # day
    row[3] = int(row[3])    # year
    row[4] = int(row[4])    # quarter

def get_quarter(month:int):
     # Get quarter based on month
    if month >= 1 and month <= 3:
        quarter = 1
    elif month >=4 and month <=6:
        quarter = 2
    elif month >=7 and month <=9:
        quarter = 3
    elif month >=10 and month <=12:
        quarter = 4
    else:
        quarter = 0
    return quarter

def save_all_sales(sales_list):
    with open(ALL_SALES, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(sales_list)

def already_imported(filename):
    with open(IMPORTED_FILES) as file:
        files = file.readlines()
        for line in files:
            line = line.replace("\n", "") # Remove newline character from each line in file
            if line == filename:
                return True
    return False

def add_imported_file(filename):
    with open(IMPORTED_FILES,"a") as file:
        file.write(f"{filename}\n")

def import_sales(filename):
    sales_list = []
    with open(filename, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            correct_data_types(row)
            sales_list.append(row)
    return sales_list
