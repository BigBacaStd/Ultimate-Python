# Python script
"""
Consider the categories of Exercise 2.14. Write end execute a script
which request the user to input two real numbers corresponding to the weight (in kilos) and the height (in meters).
Then, the script should find out how many kilos the user needs to gain/lose to arrive at a normal weight.

Example: If the weight and height input by the user are 87 and 1.70, it has to display the message:
'Your weight should be between 58.18 kilos and 72.25 kilos. You should lose 14.75 kilos' Similarly, if the weight and height
input by the user are 57 and 1.82, it has to display the message 'Your weight should be between 61.28 kilos and 82.81 kilos. You should gain 4.28 kilos'

"""

user_weight = float(input("Please enter weight in kilos: "))
user_height = float(input("Please enter height in meters: "))

bmi = user_weight / (user_height ** 2)
weight = bmi * (user_height ** 2)

min_weight = bmi * (user_height ** 2)
max_weight = bmi * (user_height ** 2)

print(min_weight)
print(max_weight)
