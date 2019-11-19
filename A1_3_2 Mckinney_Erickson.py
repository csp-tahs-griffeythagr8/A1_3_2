'''
1.3.2
Connor Mckinney
'''
import random
guess=random.randint(1,100)
def hiLo_game(guess):
    change=guess+12
    print(change)
    
"""
Spacing: 
1. Make sure to provide space after each line to improve readability. 
2. Space added between variable, assignment operator, and value/expression for guess.
3. Space added between variable, assignment operator, and value/expression for change.
You DO NOT need to add space between lines in your function. 

Guess Variable:
This is the user generated guess - we are placing our own value for testing purposes, thus while it is okay to have a random number now understand that it will be replaced by user input in the future. 

Documentation:
1. Need to use triple double quotes \"\"\" for docstrings.
2. Need to add EOL comments using a '#' to clarify purpose of main items/elements i.e. guess, hiLo_game,  change.

Not that it is necessary, however if you call the function after defining it from within the script it will run automatically once script is run. 
"""
