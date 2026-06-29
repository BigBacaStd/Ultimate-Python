# Python Script

"""
Make a dictionary containing three major rivers and the country
each river runs through. One key-Value pair might be 'nile': 'egypt'.

- User a loop to print the name of each river, such as The Nile run through Egypt.
- Use a loop to print the name of each river included in the dictionary.
- Use a loop to print the name of each country included in the dictionary.
"""

rivers = {
    'nile': 'egypt',
    'santiago': 'guadalajara',
    'cuale': 'Vallarta'
}

for name, city in rivers.items():
    print(f"The {name.title()} river runs through {city.title()}")