# Python script
# Generates a random floating-point number between 1 and 100. It also prints its data type.

import math
import random

a=random.uniform(1, 100)
b=math.floor(a+1)

print(b,type(b))