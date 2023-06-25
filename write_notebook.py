import json

notebook = {
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# Week 2: Data Types and Variables\n",
        "\n",
        "**Lesson:** Basic data types (strings, integers, floats, booleans), defining and using variables.\n",
        "\n",
        "**Activity:** Develop a program that simulates a short adventure with your favorite Super Smash Bros. character or D&D hero using user input and variables. Alternatively, create a trivia quiz about Super Smash Bros. or D&D facts using various data types.\n",
        "\n",
        "---\n",
        "\n",
        "## Example Activity for Week 2:\n",
        "\n",
        "### Activity: \"Adventure Story\" Program\n",
        "\n",
        "In this Jupyter notebook, you're going to write a program that asks the user for their favorite character, their weapon of choice, and the number of enemies they would like to face in a fictitious battle.\n",
        "\n",
        "```python\n",
        "# Ask the user for their favorite character and weapon\n",
        "character = input(\"Who is your favorite Super Smash Bros. character or D&D hero? \")\n",
        "weapon = input(f\"What weapon will {character} use in the adventure? \")\n",
        "\n",
        "# Ask the user for the number of enemies they want to face\n",
        "enemy_count = input(f\"How many enemies do you want {character} to face? \")\n",
        "\n",
        "# Print an adventure story\n",
        "print(\"\\nGreat! Here's your adventure:\")\n",
        "print(f\"{character} grabs a {weapon} and prepares to face {enemy_count} enemies. Good luck, brave warrior!\")\n",
        "```\n",
        "\n",
        "Run the code cell above. When you execute it, it will ask for your favorite game character, weapon, and the number of enemies, and then print a fun adventure story based on your inputs.\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Ask the user for their favorite character and weapon\n",
        "character = input(\"Who is your favorite Super Smash Bros. character or D&D hero? \")\n",
        "weapon = input(f\"What weapon will {character} use in the adventure? \")\n",
        "\n",
        "# Ask the user for the number of enemies they want to face\n",
        "enemy_count = input(f\"How many enemies do you want {character} to face? \")\n",
        "\n",
        "# Print an adventure story\n",
        "print(\"\\nGreat! Here's your adventure:\")\n",
        "print(f\"{character} grabs a {weapon} and prepares to face {enemy_count} enemies. Good luck, brave warrior!\")"
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.7.11"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}

# Save the notebook to a file
with open("example.ipynb", "w") as f:
    json.dump(notebook, f)