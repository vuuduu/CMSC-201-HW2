"""
File:         hw2_part2.py
Author:       Vu Nguyen
Date:         9/11/2020
Section:      31
Description:  This programs ask the user to guess the correct combination
              for the two knob on a door and the correct position on the
              switch.
"""


def rpg():
    first_knob = int(input("What is the position of the first knob (Enter 1-12)? "))
    # First Knob is in Even position
    second_knob = int(input("what is the position of the second knob (Enter 1-12)? "))
    # Second Knob is in Odd position
    switch = input("What is the position of the switch (Enter up or down)? ").lower()
    # Flip switch up

    is_1st_knob_even = False
    is_2nd_knob_odd = False
    is_flip_up = False

    if first_knob % 2 == 0:
        is_1st_knob_even = True
    if second_knob % 2 != 0:
        is_2nd_knob_odd = True
    if switch == "up":
        is_flip_up = True

    if (first_knob < 0) and (second_knob < 0):
        print("Both knob need to be set to 1 - 12!")
    elif first_knob < 0:
        print("Knob 1 needs to be set to 1 - 12!")
    elif second_knob < 0:
        print("Knob 2 needs to be set to 1 - 12!")
    else:
        if (is_1st_knob_even and is_2nd_knob_odd) and is_flip_up:
            print("The door opens, you get all the loot!")
        elif (is_1st_knob_even or is_2nd_knob_odd) or is_flip_up:
            print("The door clanks but does not open, try again.")
        else:
            print("The handle doesn't budge.")


rpg()

