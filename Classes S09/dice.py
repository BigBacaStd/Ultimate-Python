#Python script

from random import randint

"""
Make a class Die with one attribute called sides, which has a default value of 6.
Write a method called roll_die() that prints a random number between 1 and the number of sides the die
has. Make a 6-sides die and roll it 10 times.
"""
class Die:
    def __init__(self,sides = 6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


my_die = Die()
for roll_num in range(10):
    my_die.roll_die()



