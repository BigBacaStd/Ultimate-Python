#Python script

prompt = "\nSelect your pizza toppings: "
prompt += "\nEnter 'quit' when you are finished."

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)