### Exercise: Rock, Paper, Scissors Game

# Objective: Create a simple Rock, Paper, Scissors game that takes a choice from the user and the computer, then determines the winner.

import random

# --------------------------

# Instructions:
# 1. Ask the user to choose "rock", "paper", or "scissors".
# 2. Generate a random choice for the computer. Use the random library to select one of "rock", "paper", or "scissors".
# 3. Compare the user's choice and the computer's choice to determine the winner.
# 4. Print the result along with the choices made by the user and the computer.

# Example 1:
# Choose rock, paper or scissors: rock
# Computer chose: paper
# You lose!

# Example 2:
# Choose rock, paper or scissors: scissors
# Computer chose: rock
# You lose!

# Example 3:
# Choose rock, paper or scissors: rock
# Computer chose: rock
# It's a tie!

# Notes:
# - Make sure to handle invalid inputs by asking the user to choose again.
# - Use the random library to make the computer's choice unpredictable.

# Here's a bit of starter code to help you:
choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)
