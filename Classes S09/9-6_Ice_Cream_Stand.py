#Python script
"""
An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the restaurant class you wrote
in exercise 9-1 or 9-4. Either version of the class will work; just pick
the one you like better. Add an attribute called flavors that stores a list of ice cream
flavors. Write a method that displays these flavors.
Create an instance of IceCreamStand, and call this method.
"""

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
            """Print the restaurant name and cuisine type."""
            print(f"{self.restaurant_name} {self.cuisine_type}")

    def open_restaurant(self):
            """Print the restaurant is open."""
            print(f"{self.restaurant_name} is open!")

    def set_number_served(self, number):
        """Set the number of customers served to a specific value."""
        self.number_served = number

    def increment_number_served(self, addtional_customers):
        """Add the given amount to the customer reading"""
        self.number_served += addtional_customers

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours

    def show_flavours(self):
        print("We have the following flavours available: ")
        for flavour in self.flavours:
            print(f"-{flavour}")


my_ice_cream = IceCreamStand('Frosty Scoop', 'ice cream', ['vanilla', 'chocolate', 'mint'])
my_ice_cream.describe_restaurant()
my_ice_cream.show_flavours()
