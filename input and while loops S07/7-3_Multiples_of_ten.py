# Python script
"""
Ask the user for a number, and then report whether the number is a multiple of 10 or not.
"""

user_input = int(input("Please enter a number: " ))
if user_input % 10 == 0:
    print(f"The number {user_input} is multiple of 10.")

else:
    print(f"Your number {user_input} is not multiple of 10.")