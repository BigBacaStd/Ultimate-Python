#Python script

"""
A movie theater charges different ticket prices depending on a person's age. If a person is under the age of 3,
the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15, Write a loop in which you ask user's their age and then tell them the cost of their movie ticket.
"""
prompt = "\nPlease enter your age to check ticket cost(Type 'quit' to finish): "


active = True
while active:
    age = input(prompt)
    if age.lower() == 'quit':
        active = False
    else:
        age = int(age)

        if age < 3:
            print("The ticket is free.")
        elif 3 <= age < 12:
            print("Your ticket is $10")
        else:
            print("Your ticket is $15.")