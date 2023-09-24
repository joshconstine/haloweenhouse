import os
import openai
api_key = os.getenv("openaikey")

print(api_key)
print("welcome to haloween house")
import openai


# Define the conversation with system, user, and assistant messages
conversation = [
        {"role": "system", "content": "You are a helpful assistant."}
        ]

# Make the API call
response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        api_key=api_key  # Include your API key here
        )

# Extract and print the assistant's reply
assistant_reply = response['choices'][0]['message']['content']
print("Assistant:", assistant_reply)

