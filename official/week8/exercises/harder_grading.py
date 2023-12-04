# Exercise: Assign a grade to a student based on their score.

# User input
score = int(input("Enter your score (0-100): "))

# Assign grade
if score >= 90:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 or score < 80:
    print("Grade: C")
else:
    print("Grade: D or below")

# Example output
# Enter your score (0-100): 85
# Grade: B

# Enter your score (0-100): 59
# Grade: D or below

# Enter your score (0-100): 75
# Grade: C