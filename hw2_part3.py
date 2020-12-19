"""
File:         hw2_part3.py
Author:       Vu Nguyen
Date:         9/12/2020
Section:      31
Description:  A short yes/no guessing game about Star Trek. The user were
              prompt a question. They answer either yes or no and the
              output display what character the player are thinking.
"""


def star_trek():
    print("Hello! Welcome to a guessing Star Trek Characters. Player answer" +
          " should only consist of yes or no.")
    human = input("Is your character a human? ").lower()
    if human == "yes":
        captain_picard = input("Is the person bald? ").lower()
        if captain_picard == "yes":
            print("You're thinking of Captain Picard!")
        else:
            empathetic = input("Is the person empathetic? ").lower()
            if empathetic == "yes":
                print("You're thinking of Counselor Troi")
            else:
                blind = input("Is the person Blind? ").lower()
                if blind == "yes":
                    print("You're thinking of Geordi!")
                else:
                    number_one = input("Is the person Number One? ").lower()
                    if number_one == "yes":
                        print("You're thinking of Riker!")
                    else:
                        print("Shut up Wesley!")
    else:
        klingon = input("Is your character a Klingon? ").lower()
        if klingon == "yes":
            print("You're thinking of Wolf!")
        else:
            android = input("Is your character an android? ").lower()
            if android == "yes":
                print("You're thinking of Data")
            else:
                print("I don't know, Mot the Barber maybe?")


star_trek()
