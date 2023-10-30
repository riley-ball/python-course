### Exercise: Story Builder

# Objective: Create a simple story builder program that takes input from the user to fill in the blanks and then prints out the complete story.

# --------------------------

# Instructions:
# 1. Ask the user to enter a name for the main character.
# 2. Ask the user to enter an animal.
# 3. Ask the user to enter a location.
# 4. Create a story template with blanks for the main character, animal, and location.
# 5. Fill in the blanks using the user's input.
# 6. Print the complete story.

# Example 1:
# Enter the name for the main character: Tim
# Enter an animal: cat
# Enter a location: forest
# Story: 
# Once upon a time, Tim went to the forest. There, he met a friendly cat. They had an adventure of a lifetime!

# Notes:
# - Use string concatenation to assemble the final story.

# Starter Code:
main_character = None
animal = None
location = None

story_template = "Once upon a time, " + main_character + " went to the " + location + ". There, " + main_character + " met a friendly " + animal + ". They had an adventure of a lifetime!"
print("Story: ")
print(story_template)
