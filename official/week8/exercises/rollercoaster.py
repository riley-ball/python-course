# Exercise: Determine if a child is eligible for certain rides based on their height.

# If the child is between 120 and 150 centimeters, they can go on the junior roller coaster.
# If the child is 150 centimeters or taller, they can go on the giant roller coaster.
# If the child is shorter than 100 centimeters, they can go on the kiddie rides.

# User input
height = int(input("Enter your height in centimeters: "))

# Determine ride eligibility
if height > 120 and height < 150:
    print("You can go on the junior roller coaster!")
elif height >= 150 or height < 100:
    print("You can go on the giant roller coaster!")
else:
    print("You can go on the kiddie rides.")

# Example output
# Enter your height in centimeters: 130
# You can go on the junior roller coaster!

# Enter your height in centimeters: 160
# You can go on the giant roller coaster!

# Enter your height in centimeters: 90
# You can go on the kiddie rides.
