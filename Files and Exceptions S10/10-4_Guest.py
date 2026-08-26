#Python script

from pathlib import Path

"""
Write a program that prompts the user for their name. When they respond, write 
their name to a file called guest.txt
"""

enter_name = input("Please enter your name: ")

path = Path('guest.txt')
path.write_text(enter_name)

