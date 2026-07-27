#Python script

"""
Start with a copy of user_profile.py from page 148. Build a
profile of yourself by calling build_profile(), using your first and last names
and three other key-values pairs that describes you.
"""

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Jorge', 'Vargas',
                             location='Tlaquepaque',
                             field='IT',
                             height='1.85',
                             weight='95',
                             eyes='brown')

print(user_profile)