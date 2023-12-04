# Exercise: Determine the grade for a given score.

# User input
score = int(input("Enter your score (0-100): "))

# Determine grade
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
    print("Grade: E")

# Example output
# Enter your score (0-100): 85
# Grade: B

# Enter your score (0-100): 59
# Grade: F
