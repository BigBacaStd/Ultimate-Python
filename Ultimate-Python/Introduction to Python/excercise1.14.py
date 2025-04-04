# Python script
# Write and execute a script which request the user to input an integer number and computes its squared root

import math

num = float(input('Please input an integer number: '))

sqrt_num = math.sqrt(num)

print(f'The square root of {num} is: {sqrt_num:.2f}')
print(type(num))