# Python Script

# Write a Python script that:
#	1.	Asks the user to input two integers → a starting number and an ending number.
#	2.	The program must determine all perfect numbers in that range (inclusive).
#	3.	Then it should:
#	•	Print each perfect number found, and
#	•	Print the total number of perfect numbers.

Starting_Number = int(input("Please type the starting number: "))
Ending_number = int(input("Please type the ending number: "))


def is_perfect(n):
    # Return True if n is a perfect number, False otherwise
    if n < 2:  # Perfect numbers are 2 or greater
        return False

    sum_divisors = 0

    # Check all numbers from 1 to n-1 (proper divisors)
    for i in range(1, n):
        if n % i == 0:  # If 'i' divides 'n'
            sum_divisors += i

    return sum_divisors == n

#List to store perfect numbers

perfect_numbers = []

# Loop through the range and collect prime numbers

for num in range (Starting_Number, Ending_number + 1):
    if is_perfect(num):
        perfect_numbers.append(num)

# Print results

if perfect_numbers:
    print(f"\nPerfect numbers between {Starting_Number} and {Ending_number} are: ")
    for p in perfect_numbers:
        print(p)

    print(f"\nTotal of perfect numbers found are: {len(perfect_numbers)}")


else:
    print(f"There are no perfect numbers between {Starting_Number} and {Ending_number}.")
