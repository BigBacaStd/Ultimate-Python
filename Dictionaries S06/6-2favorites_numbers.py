# Python script

# Use a dictionary to store peoples favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person
# and store each as a value in your dictionary. Print each persons name and their favorite number.
# For even more fun, poll a few friends and get some actual data for your program.

favorite_numbers = {'Emily': '21', 'Ilse': '16', 'Polo': '18', 'Camila': '14', 'Elena': '9'}
for name, number in favorite_numbers.items():
    print(f"{name}´s favorite number is {number}.")

