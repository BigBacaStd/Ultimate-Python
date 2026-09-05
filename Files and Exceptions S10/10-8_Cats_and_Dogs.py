#Python script
from pathlib import Path

"""
Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file.
Write a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to cath the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a
different location on your system, and make sure the code in the except block
executes properly.
"""

try:
    path = Path('cat.txt')
    contents = path.read_text(encoding='utf8')

except FileNotFoundError:
    #print(f"Sorry, the file {path} does not exist.")
    pass
else:
    print(contents)


try:
    path = Path('dogg.txt')
    contents = path.read_text(encoding='utf8')

except FileNotFoundError:
    #print(f"Sorry, the file {path} does not exist.")
    pass

else:
    print(contents)





