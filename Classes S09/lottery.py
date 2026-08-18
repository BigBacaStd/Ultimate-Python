#Python script

from random import randint
from random import choice

"""
Make a list or tuple containing a series of 10 numbers and 5 letters.
Randomly select 4 numbers or letters from the list and print a message saying that
any ticket matching these 4 numbers or letters wins a prize
"""

list_of_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e']

winning_ticket = []

for i in range(4):
    selection = choice(list_of_numbers)
    winning_ticket.append(selection)

print(f"Any ticket matching the following numbers or letters wins a prize: {winning_ticket} ")





