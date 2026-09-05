#Python script

"""
Visit Project Gutenberg and find a few text you'd like to analyze. Download the text
filex for these works, or copy that raw text from your browser into a text file
for these works, or copy that raw text from browser into a text file on your
computer. You can use the count () method to find out how many times a word
or phrase appears in a string. For example, the following code counts the
number of times 'row' appears in a string:

line = "Row, row, row your boat"
line.count('row')

line.lower().count('row')
"""

from pathlib import Path

path = Path('alice.txt')
contents = path.read_text()

print(contents.lower().count('the'))
