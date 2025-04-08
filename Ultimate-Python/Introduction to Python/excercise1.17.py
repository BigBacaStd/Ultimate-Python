# Python script
# Execute a script which request the user to input a real positive number and displays the closest,
# previous and next integer.

import math

num = float(input('Please input a real positive number: '))
closest_int = round(num)
previous_int = closest_int - 1
next_int = closest_int + 1

print(f'The closest integer is: {closest_int}')
print(f'The previous integer is: {previous_int}')
print(f'The next integer is: {next_int}')