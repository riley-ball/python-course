# Exercise: Reverse a user-provided string and print it.

# User input
user_string = input("Enter a string to reverse it: ")

# Reverse the string
reversed_string = ""
for char in user_string:
    reversed_string = char + reversed_string

# Print result
print("Reversed string is:", reversed_string)

# Example output
# Enter a string to reverse it: Hello, World!
# Reversed string is: !dlroW ,olleH