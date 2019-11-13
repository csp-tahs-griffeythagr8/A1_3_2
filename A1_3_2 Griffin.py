"""
A1_3_2 Griffin.py
Programmer:
"""
#Creating Variables
#Create a variable 'guess'. This variable is to be assigned a value from 1-100.

guess = 52 #guess variable

#Creating Functions

def hiLo_game(guess): #hiLo_game function w/ arg guess
    change = guess - 3 #change variable holds expression 'guess-3'
    print(change)

hiLo_game(guess)
