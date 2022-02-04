"""
9-13. Dice: Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll it
10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""

from random import randint

class Die:
    """A simple attempt to represent a die."""

    def __init__(self, sides=6):
        """Initialize the attributes of a die."""
        self.sides = sides

    def roll_die(self):
        """Roll a die and output the results of the roll."""
        die_roll = randint(1,self.sides)
        print(f"You rolled a {die_roll}.")