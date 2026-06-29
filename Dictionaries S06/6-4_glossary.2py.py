# Python Script

"""
Now that you know how to loop through a dictionary, clean up the code
from exercise 6-3 by replacing your series of print () calls
with a loop that runs through the dictionary´s keys and values. When you´re
sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should
automatically be included in the output.
"""

glossary = {
    'Variable': 'A reserved memory location used to store data values that your program can manipulate. Think of it as a labeled box holding information.',
    'Function': 'A reusable block of organized code designed to perform a specific, single action. It only runs when you call its name.',
    'List': 'A built-in Python data type that holds an ordered collection of items. Lists are mutable, meaning you can change, add, or remove items after creating them.',
    'Dictionary': 'A data structure that stores data in key-value pairs rather than single values. You use a unique key to look up a corresponding value, much like looking up a word in a real dictionary.',
    'Keyword': 'Special, reserved words that have specific meanings and purposes built into Pythons syntax. Because they are reserved, you cannot use them as names for your variables or functions.'
}

for word, meaning in glossary.items():
    print(f"Word: {word}: Meaning:{meaning}")