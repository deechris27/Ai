from sentence_transformers import SentenceTransformer
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

documents = [
    "The cat sat on the mat.",
    "Artificial intelligence is transforming industries.",
    "I love hiking in the mountains.",
    "Pizza is my favorite food.",
    "She wrote a novel during the pandemic.",
    "Stock prices fell sharply yesterday.",
    "Meditation improves mental clarity and focus.",
    "Python is a versatile programming language.",
    "The sun sets beautifully over the ocean.",
    "Vaccination helps prevent diseases."
]

embeddings = model.encode(documents)

tsne = TSNE(n_components=2, perplexity=9, random_state=42)
reduced = tsne.fit_transform(embeddings)

plt.figure(figsize=(8,6))
for i, label in enumerate(documents):
    x, y = reduced[i]
    plt.scatter(x,y)
    plt.annotate(label, (x,y))
plt.title("2d embedding visualization")
plt.show()