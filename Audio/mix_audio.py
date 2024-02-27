import os

import openai
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://neyahopenai.openai.azure.com/",
    api_version="2023-06-01-preview",
    api_key=os.environ["OPENAI_API_KEY"]
)
audio_file = open("aws_lambda.mp3", "rb")

response = client.audio.translations.create(

    model="audio_demo",
    file= audio_file,
    response_format = "text"
)
response = client.chat.completions.create(
    model="text_demo",
    messages=[{"role": "user", "content": "Summarize the following text to two bullet points" +response}]

)
print(response.choices[0].message.content)




