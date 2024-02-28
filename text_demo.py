import os
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://neyahopenai.openai.azure.com/",
    api_version="2023-06-01-preview",
    api_key=os.environ["OPENAI_API_KEY"]
)

response = client.chat.completions.create(
    model="text_demo",
    messages=[{"role": "system", "content": "You are a cake baker"},
              {"role": "user", "content": "Get me a recipe to make a cake"}],
    n=3
)


for choice in response.choices:
    print(choice.message.content)

