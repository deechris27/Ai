from openai import OpenAI
import os
import numpy as np
from dotenv import load_dotenv

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    print('No API key found')
elif not api_key.startswith('sk-proj'):
    print('Invalid OpenAI api key')
else:
    print('Valid OpenAi API found!')

openai = OpenAI()

sentences = [
    "he is my friend",
    "she is a lazy girl",
    "where is the nearest airport",
    "dogs are good but need maintenance and time",
    "festive day sale is live now",
    "package needs to be returned",
    "all amazing discounts"
]

def get_embedding(text):
    res = openai.embeddings.create(input=[text], model="text-embedding-ada-002")
    return np.array(res.data[0].embedding)

embeddings = np.array([get_embedding(s) for s in sentences])

while True:
    query = input("You : ")
    if query.lower() == "exit":
        break
    query_embedding = get_embedding(query)
    from sklearn.metrics.pairwise import cosine_similarity
    similartities = cosine_similarity([query_embedding], embeddings)
    most_similar_index = np.argmax(similartities)
    print("Most similar :", sentences[most_similar_index])
