"""
File:         hw2_part5.py
Author:       Vu Nguyen
Date:         9/12/2020
Section:      31
Description:  This programs calculate the part of the eightfold path based on
              a particular angle the user enter. (Preferably divisible by 45)
"""


def enlightenment():
    angle = int(input("Enter an angle to determine the point on the Eightfold Path: "))
    if (angle % 45) != 0:
        print("You've not reached Enlightenment yet! (Try angle divisible by 45)")
    else:
        angle /= 360
        if (angle - .125) % 1 == 0:
            print("You have selected Right View!")
        elif (angle - .25) % 1 == 0:
            print("You have selected Right Samadhi!")
        elif (angle - .375) % 1 == 0:
            print("You have reached Right Mindfulness!")
        elif (angle - .5) % 1 == 0:
            print("You have selected Right Effort!")
        elif (angle - .625) % 1 == 0:
            print("You have reached Right Livelihood!")
        elif (angle - .75) % 1 == 0:
            print("You have reached Right Conduct!")
        elif (angle - .875) % 1 == 0:
            print("You have reached Right Speech!")
        else:
            print("You have reached Right Resolve!")


enlightenment()
