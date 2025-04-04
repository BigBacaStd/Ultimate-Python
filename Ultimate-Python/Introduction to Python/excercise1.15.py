# Python script
# Write and execute a script which request user to input two integer numbers from the keyboard and
# which displays the power of the first one to the second one.

import math

a= int(input('Please input the first integer: '))
b = int(input('Please input the second integer: '))

result = pow(a, b)

print(f'The power of {a} to the power of {b} is: {result}')
