# Python script
# This scripts request the user to input 5 integer numbers.
# Then the script should display the maximum and minimum numbers entered.

a=int(input('Please input the first integer: '))
b=int(input('Please input the second integer: '))
c=int(input('Please input the third integer: '))
d=int(input('Please input the fourth integer: '))
e=int(input('Please input the fifth integer: '))

maximum=max(a,b,c,d,e)
minimum=min(a,b,c,d,e)

print('The max and min  values are', maximum, 'and', minimum)