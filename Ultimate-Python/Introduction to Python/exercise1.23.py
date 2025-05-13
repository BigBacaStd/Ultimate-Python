# Python script
# Execute a script which request the user to input five integer numbers from the keyboard, then it displays the maximum.
# The script can only use one variable of type int, and no other variable.

num = int(input("Enter a number: "))  # First number initializes the variable

for _ in range(4):  # Already read 1, need 4 more
    n = int(input("Enter a number: "))  # Temporary use of the same variable
    if n > num:
        num = n  # Update if the new number is bigger

print("The highest number is:", num)

