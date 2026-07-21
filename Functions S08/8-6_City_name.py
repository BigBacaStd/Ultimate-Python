#Python script

"""
Write a function called city_country() that takes in the name of a city and its country.
The function should return a string formatted like this:

----------------------------
"Santiago, Chile"

----------------------------

Call your function with at least three city-country pairs, and print the values
that are returned.
"""

def city_country(city_name, name_country):
    """Displays information about the city"""
    return f"{city_name.title()}, {name_country.title()}"

print(city_country('santiago', 'chile'))
print(city_country('toronto', 'canada'))
print(city_country('guadalajara', 'mexico'))


