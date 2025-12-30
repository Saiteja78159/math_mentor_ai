
# import os
# import faiss
# from sentence_transformers import SentenceTransformer

# # Load embedding model
# model = SentenceTransformer("all-MiniLM-L6-v2")

# documents = []

# def load_docs():
#     base = "knowledge_base"
#     for file in os.listdir(base):
#         with open(os.path.join(base, file), "r", encoding="utf-8") as f:
#             documents.append(f.read())

# load_docs()

# # Build FAISS index
# embeddings = model.encode(documents)
# index = faiss.IndexFlatL2(embeddings.shape[1])
# index.add(embeddings)

# def retrieve_context(query: str, k=2, max_chars=400) -> str:
#     """
#     Retrieve top-k relevant knowledge chunks.
#     Returns empty string if retrieval fails.
#     """
#     if not documents:
#         return ""

#     q_emb = model.encode([query])
#     _, idxs = index.search(q_emb, k)

#     retrieved = []
#     for idx in idxs[0]:
#         retrieved.append(documents[idx][:max_chars])

#     return "\n\n".join(retrieved)


import os
import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
docs = []

for f in os.listdir("knowledge_base"):
    with open(os.path.join("knowledge_base", f), "r", encoding="utf-8") as file:
        docs.append(file.read())

emb = model.encode(docs)
index = faiss.IndexFlatL2(emb.shape[1])
index.add(emb)

def retrieve_context(query):
    q = model.encode([query])
    _, idx = index.search(q, 1)
    return docs[idx[0][0]]
