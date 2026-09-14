#Python script

"""
The remember me example only stores once piece of information, the username.
Expand this example by asking for two more pieces
of information about the user, then store all the information you collect in
a dictionary. Write this dictionary to a file using json.dumps()m and read it back
in using json.loads(). Print a summary showing exactly what your program 
remembers about the user.
"""


from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None



def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    age = input("How old are you? ")
    city = input("Where do you live? ")

    user_info = {'username': username, 'age': age, 'city': city}

    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info

def greet_user():
    """Greet the user by name."""
    path = Path('user_info.json')
    user_info = get_stored_username(path)
    if user_info:
        for key, value  in user_info.items():
            print(f"{key}: {value}")
    else:
        user_info = get_new_username(path)
        for key, value  in user_info.items():
                print(f"{key}: {value}")
        

greet_user()
