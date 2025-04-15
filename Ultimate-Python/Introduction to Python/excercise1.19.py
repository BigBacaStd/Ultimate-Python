#Python script
# This program checks if the rounded value of a number is equal to its floor or ceiling.

import math

a=float(input('Please input a positive real number: '))
b=math.floor(a)
c=math.ceil(a)

print(b==round(a))
print(c==round(a))