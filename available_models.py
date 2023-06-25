import openai

# Set up OpenAI API credentials
openai.api_key = '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'

# Call the OpenAI API to retrieve the available models
response = openai.Engine.list()

# Extract the model names from the API response
model_names = [engine['id'] for engine in response['data']]

# Print the available models
print("Available GPT models:")
for model in model_names:
    print(model)