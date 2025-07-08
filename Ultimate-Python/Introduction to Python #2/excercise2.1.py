#Python script
#Write and execute a script which request the user to input two integer numbers and a symbol.
#The script must perform a mathematical operation on the integer numbers and display the result.

num1 = int(input('Please enter the first number:'))
num2 = int(input('Please enter the second number:'))

symbol = input('Please choose a mathematical symbol (+, -, *, /):')

if symbol == '+':
    print(num1 + num2)

elif symbol == '-':
    print(num1 - num2)

elif symbol == '*':
    print(num1 * num2)

else:
    print(num1 / num2)

