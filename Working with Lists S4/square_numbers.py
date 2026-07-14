# Python Script
# Square numbers
from scipy.signal import square

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)