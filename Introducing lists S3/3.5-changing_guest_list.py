# Python Script
# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in your list.

guest_list = ['Franz Kafka', 'Milan Kundera', 'Robe Iniesta']

print(f"Dear {guest_list[0]}, I would like to invite you to eat pizza tonight.")
print(f"Dear {guest_list[1]}, I would like to invite you to eat pizza tonight.")
print(f"Dear {guest_list[2]}, I would like to invite you to eat pizza tonight.")

# TODO: Add code to handle the change in guests

guest_not_coming = guest_list[0]
guest_list.remove(guest_not_coming)
print(f"{guest_not_coming} can´t make it to the dinner.")

guest_list.append('Camus de Acuario') # Add the new guest to the list

print(f"Dear {guest_list[0]}, I would like to invite you to eat pizza tonight.")
print(f"Dear {guest_list[1]}, I would like to invite you to eat pizza tonight.")
print(f"Dear {guest_list[2]}, I would like to invite you to eat pizza tonight.")

print(guest_list)