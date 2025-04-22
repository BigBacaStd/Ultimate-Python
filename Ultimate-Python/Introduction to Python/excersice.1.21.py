# Python script
# Write and execute a script which request the user to input a real number, representing the radius of a circle,
# Then, the script should display its area and the length of its circumference.

import math

r = float(input('Please input the radius of the circle (real number):'))

area = math.pi * (r ** 2)
diameter = 2 * r
circumference = 2 * math.pi * r

print(f'The area of the circle is: {area:.2f}')
print(f'The diameter of the circle is: {diameter:.2f}')
print(f'The circumference of the circle is: {circumference:.2f}')

# Additional requirement: Validate the input to ensure that the radius is a positive real number.

