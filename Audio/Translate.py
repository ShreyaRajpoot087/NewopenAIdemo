import os

import openai
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://neyahopenai.openai.azure.com/",
    api_version="2023-06-01-preview",
    api_key=os.environ["OPENAI_API_KEY"]
)
audio_file = open("sample_french.mp3", "rb")

response = client.audio.translations.create(

    model="audio_demo",
    file= audio_file,
    response_format = "text"
)
print(response)

