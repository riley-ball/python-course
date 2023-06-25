import openai

# Set up OpenAI API credentials
openai.api_key = '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'

# Provide the chat input as messages
chat_input = [
    {"role": "system", "content": "You are a Python Tutor. Generate a comprehensive 12-week course outline for beginners to learn Python. Each week should consist of one two-hour lesson, covering essential Python concepts, and include suggestions for fun activities to reinforce the week's content."},
    {"role": "user", "content": "Generate course outline"}
]

# Call the OpenAI API to generate a chat-based response
response = openai.ChatCompletion.create(
    model="gpt-4",  # Specify the chat-based model, e.g., 'gpt-4.0-turbo'
    messages=chat_input
)

# Extract the generated response from the API response
generated_text = response.choices[0].message['content']

# Print the generated response
print(generated_text)
