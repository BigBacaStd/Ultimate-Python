#Python Script

from pathlib import Path
"""
Write a while loop that prompts user for their name.
Collect all the names that are entered, and then write these names
to a file called guest_book.txt. Make sure each entry appears
on a new line in the file.
"""
prompt = "\nPlease enter your name: "

names = ""

saved_names = []

while names != 'quit':
    names = input(prompt)
    if names != 'quit':
        saved_names.append(names)

names = "\n".join(saved_names)

path = Path('guest_book.txt')
path.write_text(names)
