#Python Script:
"""
Write and execute a script which request the user to input an integer number representing a year.
Then, it must decide whether it is (or was) a leap year,
Remark: A year number is a leap if it can be divided by 4 (with some exceptions). If
the year can be divided by 100, it is NOT a leap year unless it can be also divided by
400. This means that the year 2000 and 2400 are leap while 2100 or 2200 are not.

Example: If the user inputs the year 2004, the answer should be affirmative.
"""

IntYear = int(input("Please enter a year:"))

if (IntYear % 4 == 0) and ((IntYear % 100 != 0) or (IntYear % 400 == 0)):
    print( f"{IntYear} It is a leap year")
else:
    print(f"{IntYear} Not a leap year")