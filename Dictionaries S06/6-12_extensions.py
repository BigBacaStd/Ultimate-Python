#Python script

"""
We´re now working with examples that are complex enough
that hey can be extended in any number of ways. Use one of the examples
programs from this chapter, and extend it by adding new keys and values,
changin the context of the program, or improving the formatting of the output.
"""

pizza_styles = {
    'mexican': ['chorizo', 'onion', 'jalapeno', 'cheese'],
    'italian': ['cheese', 'pepper', 'onion', 'sausage'],
    'hawaian': ['cheese', 'pinaple', 'ham'],
}

for pizza, engridients in pizza_styles.items():
    print(f"\nPizza Styles: {pizza.title()}")
    for toppings in engridients:
        print(f"\tIngredients: {toppings.title()}")