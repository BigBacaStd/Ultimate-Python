#Python Script
#Median of three integer number

myIntA = int(input('Please input the first integer:'))
myIntB = int(input('Please input the second integer:'))
myIntC = int(input('Please input the third integer:'))

if (myIntA<=myIntB) and (myIntB<=myIntC) \
    or ((myIntC<=myIntB) and (myIntB<=myIntA)):
    print('The median is:',myIntB)

elif(myIntB<=myIntA) and (myIntA<=myIntC)\
    or ((myIntC<=myIntA) and (myIntA<=myIntB)):
    print('The median is:',myIntA)

else:
    print('The median is:',myIntC)