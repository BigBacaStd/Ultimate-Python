# Python script
# Script request user to input five integer number from the keyboard, then it displays the maximum.

numbers = []
temp = None

for _ in range(5):
    temp = int(input(f'Please input the {(_+1)} number: '))
    numbers.append(temp)


print(f'The maximum number is: {max(numbers)}')

