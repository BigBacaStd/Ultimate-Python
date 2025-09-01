#Python script
# Write and execute a script which request the user to input any number. Then, the script has to find out whether the user
# has input an integer or a real number and displayed a message.
# Example If the number input by the user is 12 0r 6.7, the message would be 'The number is an integer' or 'The introduced number is a real number', respectively.

user_input = input('Please enter a number:')

if "." in  user_input:
    print('The user input is an real number')
else:
    print('The user input in a integer number')