
import os
from dotenv import load_dotenv
import openai
import faiss
import numpy as np
from openai import OpenAI


load_dotenv(override=True)
openai_api_key = os.getenv("openai_api_key")

openai = OpenAI()

sentences = [
    "A cat sits on the windowsill.",
    "Dogs are running in the park.",
    "Birds fly across the sky.",
    "A man is walking his dog.",
    "The sunset is beautiful today."
]

def get_embedding(text):
    res = openai.embeddings.create(input=[text], model="text-embedding-ada-002")
    return np.array(res.data[0].embedding, dtype='float32')

# Step 1: Embed the sentences
embeddings = np.array([get_embedding(s) for s in sentences])

# Step 2: Store in a vector DB (FAISS index)
index = faiss.IndexFlatL2(len(embeddings[0]))  # L2 = Euclidean distance
index.add(embeddings)

# Step 3: Query something similar
query = "A man with a dog in the park"
query_embedding = get_embedding(query)

# Step 4: Search
D, I = index.search(np.array([query_embedding]), k=2)  # k = top 2 results
print("Query:", query)
print("\nTop matches: ")
for i in I[0]:
    print("****", sentences[i])
