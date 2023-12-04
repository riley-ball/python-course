# Exercise: Check if a list contains a specific element and print a message.

# List of colors
colors = ["red", "green", "blue", "yellow"]

# User input
color_to_find = input("Enter a color to check: ")

# Check for the color
if color_to_find in colors:
    print(f"The color {color_to_find} is in the list!")
else:
    print(f"The color {color_to_find} is not in the list!")
