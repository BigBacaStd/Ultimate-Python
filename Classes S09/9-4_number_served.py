#Python script

"""
Start with your program from 9.1. Add an attribute called number_served with a default value of 0.
Create an instance called restaurant from this class. Print the number of customers the restaurant has
served, and then change this value and print it again.

Add a method called set_number_served() that lets you set the number of
customers that have been served. Call this method with a new number and print
the value again.

Add a method called increment_number_served() that lets you increment
the number of customers who've been served. Call this method with any number
you like that could represent how many customers were served in, says, a day of
business.
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

# 1 Create the instance
restaurant = Restaurant('La Tomate', 'Comida Mexicana')

#2 Print the default number of customers served
print(f"Number served: {restaurant.number_served}" )

#3. Change the Value
restaurant.number_served = 25

#4. Print the new value to verify the change
print(f"Number served: {restaurant.number_served}")

#5 Print the customer that has been served

restaurant.set_number_served(50)
print(f"Number served: {restaurant.number_served}")

#6 Use increment_number_served() to add to that value
restaurant.increment_number_served(60)
print(f"Number served: {restaurant.number_served}")


