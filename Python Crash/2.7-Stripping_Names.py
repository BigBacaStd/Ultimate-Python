#Python Script
#2.7 Stripping Names: Use a variable to represent a person´s name, and include some whitespace characters at the
# beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three
# stripping functions, lstrip(), rstrip(), and strip().

persons_name = "\tPolo\n"

print("Unmodified:")
print(persons_name)

print("\nUsing lstrip():")
print(persons_name.lstrip())

print("\nUsing rstrip():")
print(persons_name.rstrip())

print("\nUsing strip():")
print(persons_name.strip())

