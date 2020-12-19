"""
File:         hw2_part4.py
Author:       Vu Nguyen
Date:         9/12/2020
Section:      31
Description:  This program which year is a leap year based on the user input
"""


def leap_year():
    year = int(input("Which year do you want to know if it is a leap year? "))
    # divisible by 4, not 100, but 400.
    if year < 0:
        print("The year is less than 1 AD/CE, we're not going back in time!!\n")
    elif (year % 4) == 0:
        if ((year % 100) != 0) or ((year % 400) == 0):
            print("This is a leap year!\n")
        else:
            print("This is Not a leap year!\n")
    else:
        print("This is not a leap year!\n")


leap_year()
