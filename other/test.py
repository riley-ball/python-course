import openai

# Set up OpenAI API credentials
openai.api_key = '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'

# Provide the chat input as messages
# chat_input = [
#     {"role": "system", "content": "You are a storyteller. Generate a story."},
#     {"role": "user", "content": "Once upon a time"}
# ]

chat_input = [
    {"role": "system", "content": "Output the input and add 3 more activity ideas related to Dungeons & Dragons, Super Smash Bros., or general gamer/nerdy themes and output the entire course outline, including the input, in the following format:\n\n# Week X: Title\n\n**Lesson:** Lesson details\n\n**Activity Ideas:**\n1. Activity 1\n2. Activity 2\n3. Activity 3"},
    {"role": "user", "content": "# Week 1: Introduction to Python\n\n**Lesson:** Introduction to Python and its history, installing Python and setting up the development environment.\n\n**Activity Ideas:**\n1. Create a program that generates random character names using Python's string manipulation capabilities.\n2. Build a simple text-based RPG game where the player can make choices and interact with different characters in a fantasy world."}
]

# Call the OpenAI API to generate text
response = openai.ChatCompletion.create(
    model="gpt-4",  # Specify the chat-based model
    messages=chat_input,
    max_tokens=300  # Specify the maximum number of tokens to generate
)

# Extract the generated text from the API response
generated_text = response.choices[0].message['content']

# Print the generated text
print(generated_text)
