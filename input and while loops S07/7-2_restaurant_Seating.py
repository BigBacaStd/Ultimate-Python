#Python script
"""
Write a program that ask the user how many people are in their dinner group.
If the answer is more than eight, print a message saying they'll have to wait for a table.
Otherwise, report that their table is ready.

"""

user_input = int(input("How many people are in your dinner group? : "))
if user_input > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready!")