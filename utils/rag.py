

import os
import faiss
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

documents = []

def load_docs():
    base = "knowledge_base"
    for file in os.listdir(base):
        with open(os.path.join(base, file), "r", encoding="utf-8") as f:
            documents.append(f.read())

load_docs()

# Build FAISS index
embeddings = model.encode(documents)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

def retrieve_context(query: str, k=2, max_chars=400) -> str:
    """
    Retrieve top-k relevant knowledge chunks.
    Returns empty string if retrieval fails.
    """
    if not documents:
        return ""

    q_emb = model.encode([query])
    _, idxs = index.search(q_emb, k)

    retrieved = []
    for idx in idxs[0]:
        retrieved.append(documents[idx][:max_chars])

    return "\n\n".join(retrieved)

