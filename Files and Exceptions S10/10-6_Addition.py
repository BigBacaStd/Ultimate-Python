#Python script

"""
One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you
try to convert to an int, you'll get a ValueError. Write a program
that prompts for two numbers. Add them together and print the result.
Catch the ValueError if either input value is not a number, and print a
friendly error message. Test your program by entering two numbers and then
by entering some text instead of a number.
"""

print("Please enter a number:")

try:
    first_number = int(input("First number: "))

    second_number = int(input("Second number: "))

    answer = first_number + second_number
    print(answer)
except ValueError:
    print("Please enter valid numbers only")

