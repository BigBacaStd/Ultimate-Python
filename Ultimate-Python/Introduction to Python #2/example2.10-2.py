#Python script
#Sorting three integer numbers

myIntA = int(input('Please input the first integer number:'))
myIntB = int(input('Please input the second integer number:'))
myIntC = int(input('Please input the third integer number:'))

if myIntA<=myIntB<=myIntC:
    print('The number in the middle is:', myIntB)

elif myIntC<=myIntB<=myIntA:
    print('The number in the middle is:',myIntB)

elif myIntC<=myIntA<=myIntB:
    print('The number in the middle is:', myIntA)

else:
    print('The number in the middle is:', myIntC)