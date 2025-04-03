# Python script
# Script request user to input a real number and displays its sine and cosine values

import math

a = float(input('Please input a real number: '))

sine_value = math.sin(a)
cosine_value = math.cos(a)

print(f'The sine of {a} is: {sine_value:.3f}')
print(f'The cosine of {a} is: {cosine_value:.3f}')