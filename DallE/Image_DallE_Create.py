import json
import os
import openai
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://neyahopenai.openai.azure.com/",
    api_version="2023-06-01-preview",
    api_key=os.environ["OPENAI_API_KEY"]
)
result =client.images.generate(
    model="image-demo",
    prompt="programmer coding on the moon",
    n=1
)
image_url= json.loads(result.model.dump.json)["images"][0]["url"]
print(image_url)