# Python script

"""
Make a class called user. Create two attributes called first_name and last_name, and then
create several other attributes that are typically stored in a use profile. Make a method
called describe_user() that prints a summary of the user's information.
Make another method called greet_user() that prints
a personalized greeting to the user.

Create several instances representing different users, and call both methods for each user.
"""

class User:
    def __init__(self, first_name, last_name, gender, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.city = city

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} {self.gender} {self.age} years old, from {self.city}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name} how are you doing today?")


the_user = User('Jorge', 'Vargas', 'Male', '37', 'Vallarta')
the_user2 = User('Ilse', 'Lopez', 'Female', '33', 'Guadalajara')

the_user.describe_user()
the_user.greet_user()
the_user2.describe_user()
the_user2.greet_user()



