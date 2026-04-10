# Python script
"""
This code prints a slice of the list. The output retains the structure of the list, and includes the first three players in the list:
"""

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])

# You can generate any subset of a list. For example, if you want the second, third, and fourth items in a list,
# you would start the silce at the index 1 and end it at index 4.
print(players[1:4])

# If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list:

print(players[:4])

# A similar syntax works if you want a slice that includes the end of a list.
# For example, if you want all items from the third item through the last item,
# you can start with index 2 and omit the second index:

print(players[2:])