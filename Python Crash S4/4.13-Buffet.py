#Python script
# 4.13 Buffet: A buffet-style restaurant only offers five basic foods. Think of five simple foods, and store them in a tuple.
# * Use a for loop to print each food the restaurant offers.
# * Try to modify one of the items, and make sure that Python produces an error.
# * The restaurant changes its menu, replacing two of the items with different foods.
# Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
# TODO: Add your code here
from scipy.signal import fir_filter_design

buffet_foods = ('Pizza', 'Burger', 'Tacos', 'Tamales', 'Sushi')

for food in buffet_foods:
    print(food)


buffet_foods = ('Huaraches', 'Burger', 'Tacos', 'Tortas')
print("\nModified Buffet menu:")
for food in buffet_foods:
    print(food)

