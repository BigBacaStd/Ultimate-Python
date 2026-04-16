#Python script
# 4.12 More Loops: All versions of foods.py in this section have avoided using for loops when printing to save space.
# Choose any example from this section, and write two for loops to print each list of foods.
# TODO: Add your code here

my_foods = ["Pizza", "Falafel", "Carrot Cake"]
friend_foods = my_foods[:]


my_foods.append("Cannoli")
friend_foods.append("Ice cream")

print("My favourite foods are:")
for food in my_foods:
    print(food)

print("\nMy friends favourite foods are:")
for food in friend_foods:
    print(food)

