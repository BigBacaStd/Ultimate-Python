# Python Script
# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# • Print a message to each of the two people still on your list, letting them know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

guest_list = ['Franz Kafka', 'Milan Kundera', 'Robe Iniesta']

print(f"Dear {guest_list[0]}, I would like to invite you to eat pizza tonight.")
print(f"Dear {guest_list[1]}, I would like to invite you to eat pizza tonight.")
print(f"Dear {guest_list[2]}, I would like to invite you to eat pizza tonight.")

# --- Handling the guest who can't make it ---
guest_not_coming = guest_list[0]
print(f"\n{guest_not_coming} can't make it to the dinner.")

# Replace the guest
guest_list[0] = 'Camus de Acuario'

# Print new invitations for the current list
print(f"\nDear {guest_list[0]}, I would like to invite you to eat pizza tonight.")
print(f"Dear {guest_list[1]}, I would like to invite you to eat pizza tonight.")
print(f"Dear {guest_list[2]}, I would like to invite you to eat pizza tonight.")

# --- Handling the bigger dinner table ---
print("\nGood news! I found a bigger dinner table!")

# Add new guests
guest_list.insert(0, 'Dee Dee Ramone') # Add to beginning
guest_list.insert(2, 'Fran Sinatra')   # Add to middle
guest_list.append('Alfredo Adame')     # Add to end

# Print invitations for everyone
print(f"\nDear {guest_list[0]}, I would like to invite you to eat pizza tonight.")
print(f"Dear {guest_list[1]}, I would like to invite you to eat pizza tonight.")
print(f"Dear {guest_list[2]}, I would like to invite you to eat pizza tonight.")
print(f"Dear {guest_list[3]}, I would like to invite you to eat pizza tonight.")
print(f"Dear {guest_list[4]}, I would like to invite you to eat pizza tonight.")
print(f"Dear {guest_list[5]}, I would like to invite you to eat pizza tonight.")

print(f"\nFinal guest list: {guest_list}")

# TODO: Add code to handle the shrinking guest list
