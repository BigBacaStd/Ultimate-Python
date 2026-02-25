#Python Script
#You can also use the remove() method to work with a value that's being removed from a list.
# Let's remove the value 'ducati' and print a reason for removing it from the list.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")