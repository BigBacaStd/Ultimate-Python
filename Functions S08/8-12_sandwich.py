#Python script

"""
Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects
as many items as the function call provides, and it should print a summary of the sandwich that's being
ordered. Call the function three times, using a different number of arguments each time.
"""

def sandwich_items(*toppings):
    """Summarize the sandwich that's being ordered"""
    print(f"\nMaking sandwich with the following toppings")
    for topping in toppings:
        print(f"-{topping.title()}")


sandwich_items('ham', 'tomato', 'cheese')
sandwich_items('ham', 'tomato', 'onions')
sandwich_items('ham', 'cheese')