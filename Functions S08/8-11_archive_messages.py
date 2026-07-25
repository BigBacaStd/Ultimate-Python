#Python script

"""
Start with your work from last exercise. Call the function send_messages() with a copy of the list of messages.
After calling the function, print both of your list to show that the original list has retained its messages.
"""

def send_messages(unsent_messages, sent_messages):
    """Simulate printing each message, until none are left"""
    while unsent_messages:
        current_message = unsent_messages.pop()
        print(f"Sending Message: {current_message}")
        sent_messages.append(current_message)

unsent_messages = ['Hello there!', 'Hey there!', 'what are you up to?']
sent_messages = []

send_messages(unsent_messages[:], sent_messages)


print(f"Final unsent messages list: {unsent_messages}")
print(f"Final sent messages list: {sent_messages}")
