#Python script

"""
Write a function that stores information about a car in a dictionary. The function should always receive
a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments.
Call the function with the required information and two other name_value pairs, such as a color
or an optional feature. Your function should work for a call like this one:

car = make_car('subaru', 'outback', color='blue', tow_pacakge=True)

print the dictionary that's returned to make sure all the information was
stored correctly
"""


def make_car(manufacturer, model, **car_specs):
    """Build a dictionary containing information about a car"""
    car_specs['manufacturer_name'] = manufacturer
    car_specs['model_name'] = model

    return car_specs


my_car = make_car('subaru', 'outback', color='blue', tow_pacakge=True)

print(my_car)

