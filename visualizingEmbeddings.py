from sentence_transformers import SentenceTransformer
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

documents = ["apple", "orange", "banana", "car", "bus", "train"]
embeddings = model.encode(documents)

tsne = TSNE(n_components=2, perplexity=2, random_state=42)
reduced = tsne.fit_transform(embeddings)

plt.figure(figsize=(8,6))
for i, label in enumerate(documents):
    x, y = reduced[i]
    plt.scatter(x,y)
    plt.annotate(label, (x,y))
plt.title("2d embedding visualization")
plt.show()