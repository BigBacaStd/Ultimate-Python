#Python script

"""
Write different versions of either exercise 7-4 or 7-5 that do each of the following at least once:
- Use a conditional test in the while statement to stop the loop
- Use an active variable to control how long the loop runs
- Use a break statement to exist the loop when the user enters a 'quit' value.
"""

prompt = "\nSelect your pizza toppings: "
prompt += "\nEnter 'quit' when you are finished."

while True:
    toppings = input(prompt)

    if toppings == 'quit':
        break
    else:
        print(f"Excellent choice! we'll add {toppings.title()} to your pizza")