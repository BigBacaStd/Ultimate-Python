#Python script
#Write an execute a script which request the user to input an integer number.
#Then the script should determine whether the number is positive, negative, or zero.

myInteger=int(input('Please input an integer number:'))

if myInteger<0:
    print('The number is negative.')
else:
    if myInteger>0:
        print('The number is positive.')
    else:
        print('The number is zero.')