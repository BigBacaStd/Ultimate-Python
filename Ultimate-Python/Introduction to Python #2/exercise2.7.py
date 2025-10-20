#Python script
"""
Write and execute a script which request user the user to input an integer number
representing a year. Then, the script has to find out which the closest leap year
following the one specified by the user. In case the user actually inputs a leap year,
it would bethe solution for the request.

Example: If the year inputs by the user is 1992 or 1993 the solution is '1992' or '1996', respectively.
"""

IntYear = int(input("Enter a year: "))

def is_leap(y):
    """Return True if y is a leap year, otherwise False."""
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

# If the input year is already a leap year, it´s the answer

if is_leap(IntYear):
    print(f"The closest leap year is {IntYear}.")
else:
    # Otherwise, find the next one
    next_year = IntYear + 1
    while not is_leap(next_year):
        next_year += 1
        print(f"The closest leap year after {IntYear} is {next_year}.")