# Python Script

#Write a Python script that:
#	1.	Asks the user to enter two integers → a starting number and an ending number.
#	2.	The program must find all prime numbers between those two numbers (inclusive).
#	3.	Then it should:
#	•	Print every prime number found, and
#	•	Print the total number of prime numbers


# 1. Ask the user to input two integers

Starting_Number = int(input("Please enter a starting number: "))
Ending_Number = int(input("Please enter an ending number: "))

# 2. Function to check if a number is prime

def is_prime(n):
    if n < 2:  # Prime numbers must be greater than 1
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check only up to √n for efficiency
        if n % i == 0:
            return False
    return True

# List to store prime numbers
prime_numbers = []


# 3. Loop through the range and collect prime numbers
for num in range(Starting_Number, Ending_Number + 1):
    if is_prime(num):
        prime_numbers.append(num)

# 4. Print results

if prime_numbers:
    print(f"\nPrime numbers between {Starting_Number} and {Ending_Number} are:")
    for p in prime_numbers:
        print(p)

    print(f"\nTotal numbers of prime numbers found: {len(prime_numbers)}")

else:
    print(f"\There are no prime numbers between {Starting_Number} and {Ending_Number}.")

