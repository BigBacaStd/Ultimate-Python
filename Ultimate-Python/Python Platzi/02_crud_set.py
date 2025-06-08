set_countries = {'Col', 'Mex', 'Bol'}

size = len(set_countries)
print(size)

print('Col' in set_countries)
print('Canada' in set_countries)

# add

set_countries.add('Canada')
print(set_countries)

# Update

set_countries.update(['Arg', 'USA', 'Peru'])
print(set_countries)

# remove

set_countries.remove('Bol')
print(set_countries)

set_countries.remove('Peru')
print(set_countries)
set_countries.discard('Peru')
print(set_countries)
set_countries.clear()
print(set_countries)
print(len(set_countries))