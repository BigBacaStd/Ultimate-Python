#Python script

"""
Add an attribute called login_attempts to your User class from 9-3.
Write a method called increment_login_attempts() that increments the value
of login_attempts by 1. Write another method called
reset_login_attempts() that resets the value of login_attempts to 0.

Make an instance of the User class and call increment_login_attempts again to make
sure it was reset to 0.
"""

class User:
    def __init__(self, first_name, last_name, gender, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} {self.gender} {self.age} years old, from {self.city}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name} how are you doing today?")

    def increment_login_attempts(self):
        """Increase login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts back to 0."""
        self.login_attempts = 0


the_user = User('Jorge', 'Vargas', 'Male', '37', 'Vallarta')
the_user2 = User('Ilse', 'Lopez', 'Female', '33', 'Guadalajara')

the_user.describe_user()
the_user.greet_user()


# Increment a few times to simulate failed login attempts

the_user.increment_login_attempts()
the_user.increment_login_attempts()
the_user.increment_login_attempts()
print(f"Login attempts: {the_user.login_attempts}")

# Reset back to 0

the_user.reset_login_attempts()
print(f"Login attempts: {the_user.login_attempts}")