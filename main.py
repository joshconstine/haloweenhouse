import os
import openai
api_key = os.getenv("openaikey")

print(api_key)
print("welcome to haloween house")
import openai

def send_user_input(input_text, conversation):
    conversation.append({"role": "user", "content": input_text})
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation,
            api_key=api_key
    )
    return response


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
# Start the while loop
while True:
    user_input = input("You: ")  # Gather user input
    conversation.append({"role": "user", "content": user_input})  
    response = send_user_input(user_input, conversation)
    assistant_reply = response['choices'][0]['message']['content']
    print("Assistant:", assistant_reply)
