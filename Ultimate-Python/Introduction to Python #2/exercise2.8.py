#Python Script

# Write and execute a script which request the user to input two integer values a and b which represent the coefficients of a first
# order equation  ax + b = 0. Then the script should display the value of the solution of the equation.
# In the cases in which there is no real solution, or in those in which there are infinite solutions, the script should display the corresponding
# message.

# Example; If the values input by the user are 2 and 3, representing the equation
# 2x + 3 = 0. the message would be 'The root of the equation is -1.5' if the value input
# by the user are 0 and 1, representing the equation 1 = 0, the script
# should display a message such as 'There are no solution'.

Value_a = int(input('Plesse enter Value a: '))
Value_b = int(input('Please enter Value b: '))

if Value_a == 0:
    if Value_b == 0:
        print("Infinite solutions.")
    else:
        print('There are no solution.')

else:
    x = -Value_b / Value_a
    print('The root of the equation is :', x)