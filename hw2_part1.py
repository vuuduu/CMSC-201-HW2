"""
File:         hw2_part1.py
Author:       Vu Nguyen
Date:         9/11/2020
Section:      31
Description:
"""


def zucchini():
    print('Welcome to the "Can we make zucchini bread today?" calculator.\n')
    brown_sugar = int(input("Enter the number of cups for brown sugar you have: "))
    # Require 1 cup of brown sugar
    white_sugar = int(input("Enter the number of cups for white sugar you have: "))
    # Require 1 cup of white sugar
    eggs = int(input("Enter the number of eggs you have: "))
    # 2 egg
    veg_oil = int(input("Enter the number of cups for vegetable oil you have: "))
    # 1 cup of veg oil
    flour = int(input("Enter the number of cups for flour you have: "))
    # 3 cup of flour
    giant_zucchini = input("Do you possess a giant zucchini? (yes/no) ").lower()

    if brown_sugar < 1:
        print("You do not have enough brown sugar!")
    elif white_sugar < 1:
        print("You do not have enough white sugar!")
    elif eggs < 2:
        print("You do not have enough eggs!")
    elif veg_oil < 1:
        print("You do not have enough vegetable oil!")
    elif flour < 3:
        print("You do not have enough flour!")
    elif giant_zucchini != "yes":
        print("You don't have a giant zucchini!")
    else:
        print("You're good to go, get baking!")


zucchini()
