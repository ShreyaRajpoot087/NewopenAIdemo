import os
from http import client

import openai
import numpy as np

openai.api_key = os.environ['OPENAI_API_KEY']


response = client.embeddings.create(
    model="embedded_demo",
    input=["hot","cold"]
)
print(response)
embeddings_1 =response.data[0].embedding
embeddings_2=response.data[1].embedding
similarity_score = np.dot(embeddings_1,embeddings_2)
print(similarity_score*100,'%')
