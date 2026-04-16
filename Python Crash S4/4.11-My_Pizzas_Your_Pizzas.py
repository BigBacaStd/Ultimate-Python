#Python script
# 4.11 My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
# * Add a new pizza to the original list.
# * Add a different pizza to the list friend_pizzas.
# * Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list.
# Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each pizza is stored in the appropriate list.
# TODO: Add your code here

my_pizzas = ['Hawaian', 'Peperoni', 'Cheese']

friend_pizzas = ['Hawaian', 'Peperoni', 'Cheese']

my_pizzas.append("Mexican")

friend_pizzas.append("Chicago Style")

print("My Favourite Pizzas are:")
for pizza in my_pizzas:
        print(pizza)

print("\nMy friend´s Favourite Pizzas are:")
for pizza in friend_pizzas:
    print(pizza)







