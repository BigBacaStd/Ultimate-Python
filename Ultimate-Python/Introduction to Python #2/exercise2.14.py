# Python Script

# Write and execute a script which request the user to input two real numbers
# corresponding to the weight (in kilos) and the height (in meters).
# The script has to find out the Body Mass Index (BMI) of the data input by the user
# Finally, the script should display a message indicating the category according to
# the following rules:

# Underweight: BMI under 18.5.
# Normal weight: BMI from 18.5 to 25.
# Overweight: BMI from 25 to 30.
# Obese Class 1: BMI from 30 to 35.
# Obese Class 2: BMI above 35.

# Remark: The formulation to compute the BMI is BMI = weight / height 2
# Example: If the weight and height input by the user are 64 and 1.65, it must
# display the message 'You are in the class: normal weight'.

user_weight = float(input("Please enter weight in kilos: "))
user_height = float(input("Please enter height in meters: "))

bmi = user_weight / (user_height ** 2)

print(f"Your calculated BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")

elif bmi <= 25:
    print("Category: Normal weight")

elif bmi <= 30:
    print("Category: Overweight")

elif bmi <= 35:
    print("Category: Obese Class 1")

else:
    print("Category: Obese Class 2")

