#Python script
# 5.9 No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
# * If the list is empty, print the message We need to find some users!
# * Remove all of the usernames from your list, and make sure the correct message is printed.
# TODO: Add your code here

usernames_list = []

if usernames_list:
    for username in usernames_list:
        print(f"Hello {username} thank you for loggin in again")
else:
    print("We need to find some users!")