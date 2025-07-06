#Python script
#Sorting three integer numbers

myIntA = int(input('Please input the first integer number: '))
myIntB = int(input('Please input the second integer number:'))
myIntC = int(input('Please input the third integer number:'))

if (myIntA<=myIntB) and (myIntB<=myIntC):
    print('The numbers in the middle is:', myIntB)

elif (myIntC<=myIntB) and (myIntB<=myIntA):
    print('The number in the middle is: ', myIntB)

elif (myIntB<=myIntA) and (myIntA<=myIntC):
    print('The number in the middle is: ', myIntA)

elif (myIntC<=myIntA) and (myIntA<=myIntB):
    print('The number in the middle is:', myIntA)

else:
    print('The number in the middle is:', myIntC)