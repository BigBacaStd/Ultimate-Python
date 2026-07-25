# Python script

"""
The function build profile() in the following example always takes in a first and last name,
but accepts an arbitrary number of keywords as well.
"""
from dataclasses import field


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] =first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)