import random
import math

"""This program generates two numbers and asks the user to provide a result using those numbers.
        What is x * y?
The program will verify and notify the user that user's answer is correct."""

a=random.randint(0,10)
b=random.randint(0,10)

userChoice = str(input("What is the answer to " + str(a) + " * " + str(b) + "\n"))

c = str(a * b)

def checkAnswer():
    """Compares the user input with the correct answer and returns confirmation of a match or mismatch"""
    if userChoice == c:
        return("Correct!")
    else:
        return ("Incorrect")


print(checkAnswer())