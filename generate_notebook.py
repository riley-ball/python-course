import openai
import json

# Set up OpenAI API credentials
openai.api_key = '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'

import re

def get_week_info():
    # Read the output.txt file
    with open('output.txt', 'r') as file:
        content = file.read()

    # Use regular expressions to extract week number, title, and lesson
    pattern = r"Week (\d+): (.+)\n\nLesson: (.+)"
    matches = re.findall(pattern, content, re.MULTILINE)

    # Create a list of dictionaries to store the week information
    weeks = []
    for match in matches:
        week_number = match[0]
        week_title = match[1]
        week_lesson = match[2]

        week_info = {
            'week_number': week_number,
            'week_title': week_title,
            'week_lesson': week_lesson
        }
        weeks.append(week_info)
    return weeks

def get_activity_info(week_info):
    prompt = f"Week {week_info['week_number']}: {week_info['week_title']}\n\nLesson: {week_info['week_lesson']}\n\n"

    chat_input = [
        {"role": "system", "content": f"Output the schedule for Week {week_info['week_number']} only and only once. Add activity ideas related \
        to Dungeons & Dragons, Super Smash Bros., or general gamer themes and so that there are 5 total. \
         Make sure the activity ideas are very easy and beginner friendly and relate to the lesson details (e.g. don't require concepts they have not learned yet).\
         Output the entire course outline, including the input, in the following format:\
        \n\n# Week {week_info['week_number']}: Title\n\n**Lesson:** Lesson details\n\n**Activity Ideas:**\n1. Activity 1\n2. Activity 2\n3. Activity 3\n4. Activity 4\n5. Activity 5"},
        {"role": "user", "content": prompt}
    ]

    # Call the OpenAI API to generate text
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Specify the chat-based model
        messages=chat_input,
        max_tokens=300  # Specify the maximum number of tokens to generate
    )

    # Extract the generated text from the API response
    generated_text = response.choices[0].message['content']

    output = generated_text
    print(output)

    # Create the notebook structure
    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [output]
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

    file_name = f"course/week{week_info['week_number']}.ipynb"

    # Save the notebook to a file
    with open(file_name, "w") as f:
        json.dump(notebook, f, indent=2)

    print(f"Course outline saved to '{file_name}' file.")

if __name__ == "__main__":
    weeks = get_week_info()
    for week in weeks:
        get_activity_info(week)