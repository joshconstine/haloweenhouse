import os
import openai
openai.api_key = os.getenv("openaikey")
audio_file = open("output.wav", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)


print(transcript.text)
