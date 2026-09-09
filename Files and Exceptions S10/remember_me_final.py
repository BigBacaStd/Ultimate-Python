#Python script

"""
The remember_me.py example only stores one piece of
information, the username. Expand this example by asking for two more
pieces of information about the user, then store all the information you collect
in a dictionary. Write this dictionary to a file using json.dumps(), and read it back
using json.loads(). Print a summary showing exactly what your programs remembers about
the user.
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
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()