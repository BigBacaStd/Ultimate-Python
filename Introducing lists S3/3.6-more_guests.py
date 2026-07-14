# Python Script
# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing people that you found a bigger dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

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
