#Python Script

places = ['Montreal', 'Vancouver', 'New York', 'Seattle', 'Calgary']

print("Here is the sorted list:")
print(sorted(places))

print("\nThis is my list in its original order:")
print(places)

print("\nThis is my list in reverse alphabetical order:")
print(sorted(places, reverse=True))

print("\nThis is my list still in its original order:")
print(places)

print("\nUsing reverse to change the order of my list:")
places.reverse()
print(places)

print("\nChanging the order again using reverse to get it back to original order:")
places.reverse()
print(places)

print("\nUsing sort to change my list so its stored in alphabetical order:")
places.sort()
print(places)

print("\nUsing sort to change list order so its stored in rever-alphabetical order:")
places.sort(reverse=True)
print(places)