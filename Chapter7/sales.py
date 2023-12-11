#!/usr/bin/env python3
"""
This module contains functions for getting
sales data from a user.
"""
def get_amount() -> float: 
    """
    Gets a sales amount greater than zero from the user,
    converts it to a float value, and returns the float
    value.
    """
    while True:
        amount = float(input("Amount:         "))
        if amount > 0:
            return amount
        else:
            print("Amount must be greater than zero.\n")

def get_month() -> int:
    """
    Gets a month between 1 and 12 from the user, converts
    it to an int value, and returns the int value.
    """
    while True:
        month = int(input("Month (1-12):   "))
        if month >= 1 and month <= 12:
            return month
        else:
            print("Month must be between 1 and 12.\n")

def get_day(month:int) -> int:
    """
    Gets a day from the user, converts it to an int
    value, and returns the int value. Based on month
    parameter, day must be between 1 and 28, 30, or 31.
    """
    if month == 2:
        max_day = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        max_day = 30
    else:
        max_day = 31

    while True:
        day = int(input(f"Day (1-{max_day}):     "))
        if day >= 1 and day <= max_day:    
            return day
        else:
            print(f"Day must be between 1 and {max_day}.\n")

def get_year() -> int:
    """
    Gets a year between 2000 and 9999 from the user,
    converts it to an int value, and returns the int value.
    """
    while True:
        year = int(input("Year:           "))
        if year >= 2000 and year <= 9999:
            return year
        else:
            print("Year must be between 2000 and 9999.\n")



    





    
