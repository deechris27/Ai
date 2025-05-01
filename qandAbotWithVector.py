# Step-by-Step Plan:

# Prepare the Knowledge Base

# Create a small list of Q&A pairs or fact sentences.

# Generate Embeddings

# Use a sentence transformer like paraphrase-MiniLM-L6-v2 to embed the knowledge base.

# Build the Vector Index

# Use FAISS to store and search through embeddings.

# Input Question

# Accept a user query and embed it.

# Similarity Search

# Retrieve the closest match from the knowledge base.

# Return the Best Answer

# Print or respond with the closest match.

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

knowledge_base = [
    "The capital of France is Paris.",
    "Python is a popular programming language for data science.",
    "The human heart has four chambers.",
    "Water boils at 100 degrees Celsius at sea level.",
    "The Sun is a star at the center of our solar system.",
    "Photosynthesis is the process by which plants make food.",
    "Mahatma Gandhi was a leader of the Indian independence movement.",
    "The Great Wall of China is visible from space is a myth.",
    "Elephants are the largest land animals on Earth.",
    "Mount Everest is the highest mountain in the world.",
    "The moon causes ocean tides due to its gravitational pull.",
    "Vitamin C helps in boosting the immune system.",
    "A healthy adult heart beats around 60 to 100 times per minute.",
    "ChatGPT is an AI model developed by OpenAI.",
    "Bats are the only mammals capable of true flight."
]

embeddings = model.encode(knowledge_base)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

while True:
    query = input("Your question : ")
    if query.lower() == "exit":
        break
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), k=1)
    for i in I[0]:
        print("Here is the matching answer from knowledge base : ", knowledge_base[i])