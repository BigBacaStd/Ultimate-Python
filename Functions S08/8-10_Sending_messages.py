#Python script

"""
Start with a copy of your program from exercise 8-9.
Write a function called send_messages() that prints each text message and
moves each message to a new list called sent_messages as it's printed.
After calling the function, print both of your list to make sure the messages were moved correctly.

"""

def send_messages(unsent_messages, sent_messages):
    """Simulate printing each message, until none are left"""
    while unsent_messages:
        current_message = unsent_messages.pop()
        print(f"Sending Message: {current_message}")
        sent_messages.append(current_message)

unsent_messages = ['Hello there!', 'Hey there!', 'what are you up to?']
sent_messages = []

send_messages(unsent_messages, sent_messages)


print(f"Final unsent messages list: {unsent_messages}")
print(f"Final sent messages list: {sent_messages}")


