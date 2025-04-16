#Python script
# This code extracts the decimal part of a positive real number, scales it by 100,
# and rounds it up to get the smallest integer greater than or equal to the hundredths value.


import math

a=float(input('Please input a positive real number: '))
a=a-math.floor(a)
b=math.ceil(a * 100)

print(b)