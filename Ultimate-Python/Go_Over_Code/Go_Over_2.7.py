# Python Script:

# Write a Python script that asks the user to input an integer number representing a year. Then, the program must find the closest previous leap year.
#	-	If the year entered by the user is already a leap year, the program should say so.
#	-	If the year is not a leap year, your program should go backwards year by year until it finds the most recent leap year.



IntYear = int(input("Please enter a year: "))


def is_leap(y):
    """Return True if y is a leap year, otherwise False."""
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)


#	-	If the year entered by the user is already a leap year, the program should say so.

if is_leap(IntYear):
    print(f"The closest leap year is {IntYear}.")

else:
    # Otherwise, find the next one
    previous_year = IntYear - 1
    while not is_leap(previous_year):
        previous_year -= 1


    print(f"The closest leap year before {IntYear} is {previous_year}.")
