#Python script

from city_functions import city_country_name

def test_city_name():
    formatted_name = city_country_name('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'

def test_city_country_population():
    formatted_name = city_country_name(
        'santiago', 'chile', '5000000')
    assert formatted_name == 'Santiago, Chile - Population 5000000'