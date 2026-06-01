#Python script
# 5.11 Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# * Store the numbers 1 through 9 in a list.
# * Loop through the list.
# * Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.
# Your output should be "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
# TODO: Add your code

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for numbers in numbers:
    if '1' in numbers:
        print(f"{numbers}St.")
    elif '2' in numbers:
        print(f"{numbers}nd.")
    elif '3' in numbers:
        print(f"{numbers}rd.")
    else:
        print(f"{numbers}th")
