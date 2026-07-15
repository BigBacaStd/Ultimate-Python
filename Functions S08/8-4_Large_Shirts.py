#Python script

"""
Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different
message.
"""

def make_shirt(shirt_size='Large', shirt_message='I love Python'):
    print(f"\nShirt size is: {shirt_size} and the message on the shirt says: {shirt_message}")


make_shirt()
make_shirt(shirt_size='Medium')
make_shirt(shirt_size='Small', shirt_message='Python rules the world!')