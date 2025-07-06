#Python script
#Checking the validity of a day-month date

myDay=int(input('Please input the day number:'))
myMonth=int(input('Please input the month number:'))

if myMonth==2:
    maxDay=28
elif myMonth==4\
    or myMonth==6\
    or myMonth==9\
    or myMonth==11:
    maxDay=30
else:
    maxDay=31

if 1<=myDay and myDay<=maxDay:
    print('The date is valid.')
else:
    print('The date is invalid')