# Exercise: Print the multiplication table for a given number.

# User input
number = int(input("Enter a number to see its multiplication table: "))

# Print multiplication table
for i in range(1, 11):
    print(f"{number} x {i} = {number * i")

# Example output
# Enter a number to see its multiplication table: 5
# 5 x 1 = 5