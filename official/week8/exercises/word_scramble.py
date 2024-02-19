# Exercise: Create a word scramble game. Scramble the letters of a word and ask the user to guess the original word.

import random

# Word to scramble
word = "python"
scrambled = list(word)
random.shuffle(scrambled)
scrambled = ''.join(scrambled)

# User guesses the word
print("Scrambled word:", scrambled)
user_guess = input("Guess the original word: ")

# TODO: Write a loop to give the user multiple attempts or until they guess correctly

# Example Output:
# Scrambled word: nhtopy
# Guess the original word: python
# Correct!
