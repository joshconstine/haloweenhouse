import os
import openai
import pyaudio
import wave
api_key = os.getenv("openaikey")

audio = pyaudio.PyAudio()
#configure thr Microphone input
audio_format = pyaudio.paInt16  # Audio format (16-bit)
sample_rate = 16000             # Sample rate (adjust as needed)
channels = 1                    # Number of audio channels (1 for mono)
chunk=1024

microphone_stream = audio.open(
        format=audio_format,
        channels=channels,
        rate=sample_rate,
        input=True,
        frames_per_buffer=chunk # Adjust buffer size as needed
)

print("start recording...")

frames=[]
seconds = 3

for i in range(0, int(sample_rate / chunk * seconds)):
    data = microphone_stream.read(chunk)
    frames.append(data)

print("recording stopped")

microphone_stream.stop_stream()
microphone_stream.close()
audio.terminate()


wf = wave.open("output.wav", 'wb')
wf.setnchannels(channels)
wf.setsampwidth(audio.get_sample_size(audio_format))
wf.setframerate(sample_rate)
wf.writeframes(b''.join(frames))
wf.close()



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
