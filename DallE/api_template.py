import os
import openai

openai.api_type = "azure"
openai.api_base = "https://neyahopenai.openai.azure.com/"
openai.api_version = "2023-06-01-preview"
openai.api_key = os.environ["OPENAI_API_KEY"]
