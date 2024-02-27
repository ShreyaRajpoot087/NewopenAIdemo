import os
import openai

openai.api_key = os.environ['OPENAI_API_KEY']

response = openai.Embedding.create(
    input="Learn share and grow",
    model="text-embedding-ada-002"

)
emdeddings_1= response['data'][0]['embedding']
emdeddings_2= response['data'][1]['embedding']

similarity_score =np.dot(emdeddings_1,emdeddings_2)
print(similarity_score*100,"%")
