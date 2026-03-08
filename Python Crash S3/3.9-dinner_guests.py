# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page 42),
# use len() to print a message indicating the number of people you are inviting to dinner.

guest_list = ['Franz Kafka', 'Milan Kundera', 'Robe Iniesta']
print(len(guest_list))

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

print("Hey there! Unfortunately I can only invite 2 people for dinner. I am sorry!")

guest_not_invited = guest_list.pop()
print(f"I am sorry {guest_not_invited.title()}, you were un-invited to my dinner")

guest_not_invited = guest_list.pop()
print(f"I am sorry {guest_not_invited.title()}, you were un-invited to my dinner")

guest_not_invited = guest_list.pop()
print(f"I am sorry {guest_not_invited.title()}, you were un-invited to my dinner")

guest_not_invited = guest_list.pop()
print(f"I am sorry {guest_not_invited.title()}, you were un-invited to my dinner")

print(f"Dear {guest_list[0]}, I would like to let you know that you are still invited to my dinner.")
print(f"Dear {guest_list[1]}, I would like to let you know that you are still invited to my dinner.")

del guest_list[0]
del guest_list[0]

print(guest_list)
