#Python script
#Reading different types of numbers

myChar=input('Please specify a letter - (r / i ):')

if myChar=='r':
    myNumber=float(input('Please input a real number:'))
    print('The value', myNumber, 'is of', type(myNumber))
elif myChar=='i':
    myNumber=int(input('Please input an integer number:'))
    print('The value', myNumber, 'is of', type(myNumber))
else:
    print('The user mistyped the letter, sorry')