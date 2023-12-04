# Exercise: Check if a user is eligible to enter a competition based on their age and location.

# Anyone older than 18 is eligible to enter the competition, regardless of their location.

# User input
age = int(input("Enter your age: "))
location = input("Enter your location (city): ")

# Check eligibility
if age > 18 and location.lower() == 'new york':
    print("You are eligible to enter the competition.")
else:
    print("You are not eligible to enter the competition.")  # Bug here

# Example output
# Enter your age: 19
# Enter your location (city): New York
# You are eligible to enter the competition.

# Enter your age: 19
# Enter your location (city): Australia
# You are eligible to enter the competition.