# Magic Number Guessing Game

import random

# Initializing a random number between 1 and 10
magic_number = random.randint(1, 10)

# --------------------------
# Exercise: Ask the user to guess the magic number. Inform them if their guess is correct or not.
# Hint: Remember to convert the input to an integer before comparison.
# TODO: Write your code below this line

user_guess = int(input("Guess the magic number between 1 and 10: "))
if user_guess == magic_number:
    print("Congratulations! You guessed the magic number!")
else:
    print("Sorry, that's not the magic number. Better luck next time!")

# TODO: Write your code above this line
# --------------------------
