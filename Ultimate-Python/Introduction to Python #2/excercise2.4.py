#Python script
#Sorting three integer numbers

myIntA = int(input('Please input the first integer'))
myIntB = int(input('Please input the second integer'))
myIntC = int(input('Please input the third integer'))

if (myIntA<myIntB) and (myIntA<myIntC):
    if myIntB<=myIntC:
        print('The number in the middle is:',myIntB)
    else:
        print('The number in the middle is:',myIntC)

elif (myIntB<=myIntA) and (myIntB<=myIntC):

    if myIntA<=myIntC:
        print('The number in the middle is:',myIntA)
    else:
        print('The number in the middle:',myIntC)

else:
    if myIntA<=myIntB:
        print('The number in the middle is:',myIntA)
    else:
        print('The number in the middle is:',myIntB)