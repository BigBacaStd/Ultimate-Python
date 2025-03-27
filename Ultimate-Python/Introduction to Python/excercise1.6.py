#Python script
#Generates 2 ramdom numbers

import random

upperLimit=100.0
lowerLimit=0.0

a=random.uniform(lowerLimit, upperLimit)
b=random.uniform(lowerLimit, upperLimit)

result=a/b

print('The values are %.3f and %.3f' %(a,b))
print('%.3f'%result)
print(type(result))