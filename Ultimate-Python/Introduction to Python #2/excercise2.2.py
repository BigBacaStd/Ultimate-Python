#Python script
#Write and execute a script which request the user to input three integer numbers in any order
#then, it must display a message whether they can be sorted as to create a Pythagorean triple or not.

a = int(input('Please enter the first number: '))
b = int(input('Please enter the second number: '))
c = int(input('Please enter the third number: '))

def is_pythagorean_triple(x, y, z):
    a,b,c = sorted([x,y,z])
    return a**2 + b**2 == c**2

if is_pythagorean_triple(a, b, c):
    print('They are Pythagorean triple')

else:
    print('They are not Pythagorean Triple')