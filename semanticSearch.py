


from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

documents = ["Odin is a sweet pet dog", "He was a stock broker", "He was obedient", "Who is Lakhan lal's son"]
embeddings = model.encode(documents)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

while True:
    query = input("You : ")
    if query.lower() == "exit":
        break
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), k=2)
    for i in I[0]:
        print("Matches :", documents[i])

