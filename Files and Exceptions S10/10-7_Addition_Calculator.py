#Python script

"""
Wrap your code from exercise 10-5 in a while loop
so the user can continue entering numbers, even if they make a mistake and
enter text instead of a number.
"""

print("Please enter a number:")
print("Type 'q' to finish.")

while True:
    try:
        first_number = input("First number: ")
        if first_number == 'q':
            break

        second_number = input("Second number: ")
        if second_number == 'q':
            break

        answer = int(first_number) + int(second_number)
        print(answer)
    except ValueError:
        print("Please enter valid numbers only")