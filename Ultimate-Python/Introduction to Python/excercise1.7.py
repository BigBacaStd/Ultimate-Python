#Python script
#Generates 2 ramdom numbers

import random

upperLimit=100
lowerLimit=0

a=random.randint(lowerLimit, upperLimit)
b=random.randint(lowerLimit, upperLimit)

result=a//b

print('The values are',a,b)
print(result)
print(type(result))