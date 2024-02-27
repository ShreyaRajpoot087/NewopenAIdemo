import os

import openai
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://neyahopenai.openai.azure.com/",
    api_version="2023-06-01-preview",
    api_key=os.environ["OPENAI_API_KEY"]
)
audio_file = open("sample_english_audio.wav", "rb")
response =openai.Audio.Transcribe(
 model ="whisper-1",
 file= audio_file,
 language="en-US",
 response_format="text"
)
print(response)
