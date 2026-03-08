# 3-10. Every Function: Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

# Topic: Skateboard Brands

skateboard_brands = ['Santa Cruz', 'Powell Peralta', 'Element', 'Girl', 'Chocolate']

print("Original list:")
print(skateboard_brands)

# TODO: Use append() to add a brand to the end
skateboard_brands.append('Flip')
print(skateboard_brands)
# TODO: Use insert() to add a brand at a specific position

skateboard_brands.insert(2,'Baker')
print(skateboard_brands)
# TODO: Use del to remove a brand by index
del skateboard_brands[4]
print(skateboard_brands)

# TODO: Use pop() to remove the last brand (and print it)
popped_skateboard = skateboard_brands.pop()
print(skateboard_brands)
print(popped_skateboard)
# TODO: Use remove() to remove a brand by value
skateboard_brands.remove('Element')
print(skateboard_brands)
# TODO: Use sort() to permanently sort the list alphabetically
skateboard_brands.sort()
print(skateboard_brands)
# TODO: Use sort(reverse=True) to permanently sort the list in reverse alphabetical order
skateboard_brands.sort(reverse=True)
print(skateboard_brands)
# TODO: Use sorted() to temporarily sort the list
print(sorted(skateboard_brands))

# TODO: Use reverse() to reverse the order of the list
skateboard_brands.reverse()
print(skateboard_brands)
# TODO: Use len() to find the length of the list
print(len(skateboard_brands))
