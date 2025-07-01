#Python script
#Checking the sign of two real numbers

myRealA=float(input('Please input a float number:'))
myRealB=float(input('Please input another float number: '))

if ((myRealA>0) and (myRealB>0)) or ((myRealA<0) and (myRealB<0)):
    print('They have the same sign.')
else:
    print('They have mixed signs.')