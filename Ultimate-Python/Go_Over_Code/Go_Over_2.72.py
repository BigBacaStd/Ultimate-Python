# Python Script

# Write a Python script that:
#	1.	Asks the user to input two years: a starting year and an ending year.
#	2.	The program must determine how many leap years exist between those two years (inclusive).
#	3.	Then it should print each leap year found and the total number of leap years.

Start_Year = int(input("Please enter the start year: "))
End_Year = int(input("Please enter the end year: "))


def is_leap(y):
    """Return True if y is a leap year, otherwise False."""
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

leap_years = []

for year in range(Start_Year, End_Year + 1):
    if is_leap(year):
        leap_years.append(year)

if leap_years:
    print(f"\nLeap years between {Start_Year} and {End_Year} are:")
    for year in leap_years:
        print(year)


    print(f"\nTotal number of leap years found: {len(leap_years)}")
else:
        print(f"There are no leap years between {Start_Year} and {End_Year}.")