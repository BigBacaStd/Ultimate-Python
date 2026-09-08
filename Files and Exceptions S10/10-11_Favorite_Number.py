#Python Script

"""
Write a program that prompts for the user's favorite
number: Use json.dumps() to store this number in a file.
Write a separate program that reads in this value and prints the
message "I know your favorite number! It's ___."
"""

from pathlib import Path
import json

favorite_number = input("What's your favorite number: ")

path = Path('favorite_number.json')
contents = json.dumps(favorite_number)
path.write_text(contents)

print(f"We'll remember you when you come back!")