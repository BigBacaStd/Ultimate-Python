#Python script

"""
Write a function called describe_city() that accepts the name of a city and its country. The function
should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the default country.
"""

def describe_city(city_name, city_country='Iceland'):
    print(f"\n{city_name} is in {city_country}")

describe_city(city_name='Reykjavik')
describe_city(city_name='Akureyri')
describe_city(city_name='Toronto', city_country='Canada')