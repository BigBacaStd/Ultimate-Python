# Python script

"""
Start with your class from 9-1. Create three different instances from the class, and call describe_restaurant()
for each instance.
"""

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
            """Print the restaurant name and cuisine type."""
            print(f"{self.restaurant_name} {self.cuisine_type}")

    def open_restaurant(self):
            """Print the restaurant is open."""
            print(f"{self.restaurant_name} is open!")


the_restaurant = Restaurant('La Tomate', 'Comida Mexicana')
the_restaurant2 = Restaurant('Los Tarascos', 'Tacos al Pastor')
the_restaurant3 = Restaurant('La Macaria', 'Especialidades Mexicanas')


the_restaurant.describe_restaurant()
the_restaurant2.describe_restaurant()
the_restaurant3.describe_restaurant()