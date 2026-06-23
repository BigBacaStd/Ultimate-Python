# Python script

"""
A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, lets call it glossary.

- Think of five programming words you have learned about the previous
  chapters. Use these words as the keys in your glossary, and store their
  meanings as values.

- Print each word and its meaning as neatly formatted output. You might
  print the word followed by a colon and then its meaning, or print the word
  on one line and then print its meaning indented on a second line. Use the
  newline character (\n) to insert a blank line between each word-meaning
  pair in your output
"""

glossary = {
    'Variable': 'A reserved memory location used to store data values that your program can manipulate. Think of it as a labeled box holding information.',
    'Function': 'A reusable block of organized code designed to perform a specific, single action. It only runs when you call its name.',
    'List': 'A built-in Python data type that holds an ordered collection of items. Lists are mutable, meaning you can change, add, or remove items after creating them.',
    'Dictionary': 'A data structure that stores data in key-value pairs rather than single values. You use a unique key to look up a corresponding value, much like looking up a word in a real dictionary.',
    'Keyword': 'Special, reserved words that have specific meanings and purposes built into Pythons syntax. Because they are reserved, you cannot use them as names for your variables or functions.'
}

for word, meaning in glossary.items():
    print(f"{word}: \n{meaning}")

