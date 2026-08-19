#Python script
from random import choice

"""
You can use a loop to see how hard it might be to win
the kind of lottery you just modeled. Make a list or tuple called my_ticket.
Write a loop that keeps pulling numbers until your ticket wins.
Print a message reporting how many times the loop had to run to give you a winning ticket.
"""

list_of_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e']

my_ticket = []

counter = 0

for i in range(4):
    selection = choice(list_of_numbers)
    my_ticket.append(selection)

won = False

while not won:
    counter +=1
    new_draw = []

    for i in range(4):
        selection = choice(list_of_numbers)
        new_draw.append(selection)


    if my_ticket == new_draw:
        won = True


print(f"My ticket with the numbers: {my_ticket} won a prize, it took me {counter} times to win!")

