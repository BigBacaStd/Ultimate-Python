# Write a Python script that:
# 	•	Accepts 7 numbers from the user (one at a time).
# 	•	Uses only one variable throughout the script.
# 	•	Prints only the lowest number entered.

num = int(input("Enter a number: ")) # First number initializes the variable

for _ in range(6): # Already read 1, need 6 more
    n = int(input("Enter a number: ")) # Temporary use of the same variable
    if n < num:
        num = n # Update if the new number is lower


print("The lowest number is:", num)