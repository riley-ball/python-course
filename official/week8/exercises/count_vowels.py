# Exercise: Count the number of vowels in a user-provided string.

# User input
user_string = input("Enter a string: ")

# Count vowels
vowels = "aeiou"
count = 0
for char in user_string:
    if char in vowels:
        count =+ 1

# Print result
print(f"Number of vowels in the string: {count}")

# Example output
# Enter a string: Hello, World!
# Number of vowels in the string: 3