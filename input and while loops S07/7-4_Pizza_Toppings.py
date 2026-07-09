#Python script

"""
Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
As they enter each topping, print a message saying you'll add that topping to their pizza.
"""
prompt = "\nPlease enter your pizza toppings (Type 'quit' to finish.): "


while True:
    topping = input(prompt)


    if topping.lower() == 'quit':
        break
    else:
        print("Great choice! We will add it to your pizza!")