### Exercise: Rock, Paper, Scissors Game

import random  # Importing the random library to generate random choices

# Instructions:
# 1. Ask the user to choose "rock", "paper", or "scissors".
# 2. Generate a random choice for the computer.
# 3. Compare the user's choice and the computer's choice to determine the winner.
# 4. Print the result along with the choices made by the user and the computer.

# Starter code:
choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)

# Asking for user input
user_choice = input("Choose rock, paper or scissors: ").lower()
print(f"Computer chose: {computer_choice}")

# Determining the winner
if user_choice == computer_choice:
    print("It's a tie!")
    
# User chooses rock
elif user_choice == "rock" and computer_choice == "scissors":
    print("Rock smashes scissors! You win!")
elif user_choice == "rock" and computer_choice == "paper":
    print("Paper covers rock! You lose!")
# User chooses paper
elif user_choice == "paper" and computer_choice == "rock":
    print("Paper covers rock! You win!")
elif user_choice == "paper" and computer_choice == "scissors":
    print("Scissors cut paper! You lose!")
# User chooses scissors
elif user_choice == "scissors" and computer_choice == "paper":
    print("Scissors cut paper! You win!")
elif user_choice == "scissors" and computer_choice == "rock":
    print("Rock smashes scissors! You lose!")