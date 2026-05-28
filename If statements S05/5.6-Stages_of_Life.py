#Python script
# 5.6 Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
# * If the person is less than 2 years old, print a message that the person is a baby.
# * If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# * If the person is at least 4 years old but less than 13, print a message that the person is a kid.
# * If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
# * If the person is at least 20 years old but less than 65, print a message that the person is an adult.
# * If the person is age 65 or older, print a message that the person is an elder.
# TODO: Add your code here

user_age = 70

if user_age < 2:
    print("This person is a baby")
elif user_age == 2 or user_age < 4:
    print("This person is a toddler")

elif user_age == 4 or user_age < 13:
    print("This person is a kid")

elif user_age == 13 or user_age < 20:
    print("This person is a teenager")

elif user_age == 20 or user_age < 65:
    print("This person is an adult")

else:
    print("This person is an elder")