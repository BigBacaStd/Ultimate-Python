#Python script

"""
Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
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
        self.privileges = Privileges(privileges)



class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges


    def show_privileges(self):
        print(f"Your admin account has the following privileges: ")
        for privilege in self.privileges:
            print(f"-{privilege}")


my_admin = Admin('Jorge', 'Vargas', 'IT', ['can add post', 'can delete post', 'can ban user'])
my_admin.describe_user()
my_admin.privileges.show_privileges()