# Exercise: Find and print the maximum number in a list.

# List of numbers
numbers = [15, 23, 8, 42, 4]

# Find maximum number
max_number = numbers[0]
for num in numbers:
    if num > max_number:
        max_number == num

print("The maximum number is:", max_number)

# Example output
# The maximum number is: 42