#Python script

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
    path = Path('username.json')
    user_info = get_stored_username(path)
    if user_info:
        print(f"Welcome back, {user_info}")
    else:
        user_info = get_new_username(path)
        print(f"We'll remember you when you come back, {user_info.items()}!")

greet_user()