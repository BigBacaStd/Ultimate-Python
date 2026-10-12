#Python script

"""
When you roll the three D6 dice, the smallest number you can roll is 3 and the largest number is 18.
Create a visualization that shows you what happens when you roll three D6 dice.
"""

from random import randint


class Die:
    """A class representing a single die."""
    def __init__(self, num_sides=6):
        """Assume an eight-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)

