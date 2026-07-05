#Python script

"""
Modify your program from exercise 6.2 so each person can have more than one favorite number. Then print each person's
name along with their favorite numbers.
"""

favorite_numbers = {

    'Emily': ['21', '14'],
    'Ilse': ['16', '93'],
    'Polo': ['18', '21'],
    'Camila': ['23', '14'],
    'Elena': ['17', '31'],
}

for person, fav_number in favorite_numbers.items():
    print(f"{person.title()}'s favorite numbers are:")
    for number in fav_number:
        print(f"{number}")