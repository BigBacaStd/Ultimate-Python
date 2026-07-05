#Python script

"""
Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each
city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city´s dictionary
should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.

"""
cities = {
    'toronto': {
      'country':'canada',
        'population': '4m',
        'fact': 'cn tower',
    },
    'vancouver': {
        'country': 'canada',
        'population': '2m',
        'fact': 'whistler',
    },

    'montreal': {
        'country': 'canada',
        'population': '5m',
        'fact': 'mount royal',

    },
}

for c_name, c_info in cities.items():
    print(f"{c_name.title()}")

    print(f"Country:{c_info['country'].title()}")
    print(f"Population: {c_info['population']}")
    print(f"Fact: {c_info['fact'].title()}")
    print("--------------")
