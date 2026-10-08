from random import randint

"""
Create a simulation showing what happens when you roll two eight-side dice 1,000. Try to picture
what you think the visualization will look like before you run the simulation, then see if your 
intuition was correct.

Gradually increase the number of rolls until you start to see the limits of your
system's capabilities.

"""

class Die:
    """A class representing a single die."""
    def __init__(self, num_sides=8):
        """Assume an eight-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)
