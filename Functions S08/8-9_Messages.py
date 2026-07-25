#Python script

"""
Make a list containing a series of short text messages. Pass the list function called show_messages(), which prints each text message.

"""

messages = ['Hello there!', 'Hey there!', 'what are you up to?']

def show_messages(messages):
    """Show all messages"""
    print(f"The following messages have been sent")
    for message in messages:
        print(f"-{message}")

show_messages(messages)

