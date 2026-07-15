#Python script

"""
Write a function called make_shirt() that accepts a size and the text of a message that
should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the
message printed on it.

Call the function once using positional arguments to make a shirt. Call the function
a second time using keyword arguments.
"""
def make_shirt(shirt_size, shirt_message):
    print(f"\nShirt size is: {shirt_size} and the message on the shirt says: {shirt_message}")

make_shirt('Medium', 'The Ramones')
make_shirt('Large', 'I love Python!')