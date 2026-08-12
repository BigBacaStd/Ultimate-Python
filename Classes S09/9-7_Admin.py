#Python script

"""
An administrator is a special kind of user. Write a class called
Admin that inherits from the user class you wrote in 9-3 or 9-5.
Add an attribute, privileges, that stores a link of strings like
"can add post", "can delete post", "can ban user", and so on.

"""

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")


class Admin(User):
    def __init__(self, first_name, last_name, department, privileges):
        super().__init__(first_name, last_name)
        self.department = department
        self.privileges = privileges

    def show_privileges(self):
        print(f"Your admin account has the following privileges: ")
        for privileges in self.privileges:
            print(f"-{privileges}")

my_admin = Admin('Jorge', 'Vargas', 'IT', ['can add post', 'can delete post', 'can ban user'])
my_admin.describe_user()
my_admin.show_privileges()
