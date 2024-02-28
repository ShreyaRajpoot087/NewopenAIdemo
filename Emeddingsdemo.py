import os
import openai

from Embeddings.Emeddings_demo import client

openai.api_key = os.environ['OPENAI_API_KEY']

response = client.embeddings.create(
    model="embedded_demo",
    input="cat"
)
print(response)
