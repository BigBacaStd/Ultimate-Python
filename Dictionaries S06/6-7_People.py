#Python script

"""
Start with the program you wrote for exercise 6.1. Make
two new dictionaries representing different people, and store all three dictionaries in a list called people.
Loop through your list of people. As you loop through the list, print everything you know about each person.
"""

people = {
    'person_1': {
        'first_name': 'emily',
        'last_name': 'vargas',
        'city': 'vallarta',
    },
    'person_2': {
        'first_name': 'ilse',
        'last_name': 'lopez',
        'city': 'guadalajara',
    },
    'person_3': {
        'first_name': 'camila',
        'last_name': 'vargas',
        'city': 'Sault Ste Marie',
    },
}

for person_number, user_info in people.items():
    print(f"\nPerson number {person_number}")
    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    location = user_info['city']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

