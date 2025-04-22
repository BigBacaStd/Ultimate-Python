# Python script
# Calculate Circle Radius, Diameter, and Area from Circumference

import math

c = float(input('Please input the circumference of the circle:'))

# Formulas:
r = c / (2 * math.pi)              # Radius
d = 2 * r                          # Diameter
a = math.pi * (r ** 2)            # Area

print(f'The radius of the circle is: {r:.2f}')
print(f'The diameter of the circle is: {d:.2f}')
print(f'The area of the circle is: {a:.2f}')

# Additional requirement: Validate the input to ensure that the circumference is a positive real number.