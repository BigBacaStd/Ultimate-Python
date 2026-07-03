#Python script
"""
Make several dictionaries, where each dictionary represents a different pet.
In each dictionary, include the kind of animal and the owner´s name.
Store these dictionaries ina list called pets. Next, loop through your list and as
you do, print everything you know about each pet.
"""

pet_1 = {
    'kind': 'cat',
    'pet_name': 'dominga',
    'owners_name': 'polo',
}

pet_2 = {
    'kind': 'dog',
    'pet_name': 'tulio',
    'owners_name': 'ilse',
}

pet_3 = {
    'kind': 'bird',
    'pet_name': 'peri',
    'owners_name': 'emily',
}

pets = [pet_1, pet_2, pet_3]

for pet_info in pets:

    print(f"\nPet kind: {pet_info['kind'].title()}")
    print(f"Pet name: {pet_info['pet_name'].title()}")
    print(f"Owner´s name: {pet_info['owners_name'].title()}")
