### Exercise: Rock, Paper, Scissors Game

import random  # Importing the random library to generate random choices

# --------------------------

# Instructions:
# 1. Ask the user to choose "rock", "paper", or "scissors".
# 2. Generate a random choice for the computer.
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

# Starter code:
choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)

# Asking for user input
user_choice = input("Choose rock, paper or scissors: ").lower()
print(f"Computer chose: {computer_choice}")

# Determining the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") \
        or (user_choice == "paper" and computer_choice == "rock") \
        or (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("You lose!")
