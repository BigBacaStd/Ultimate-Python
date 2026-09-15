#Python
"""
The final listing for remember_me.py assumes either that the user has already
entered their username or that the program is running for the first time.
We should modify it in case the current user is not the person
who last used the program.

Before printing a welcome back message in greet_user(), ask the user if
this is the correct username. If it's not, call get_new_user() to get
the correct username.
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
        verification = input(f"Are you {user_info['username']}? (y/n)")
        if verification == 'y':
            for key, value in user_info.items():
                print(f"{key}: {value}")
        else:
            user_info = get_new_username(path)
            for key, value in user_info.items():
                print(f"{key}: {value}")





    else:
        user_info = get_new_username(path)
        for key, value in user_info.items():
            print(f"{key}: {value}")


greet_user()