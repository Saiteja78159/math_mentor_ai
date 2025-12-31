
# # # # # import os
# # # # # import faiss
# # # # # from sentence_transformers import SentenceTransformer

# # # # # # Load embedding model
# # # # # model = SentenceTransformer("all-MiniLM-L6-v2")

# # # # # documents = []

# # # # # def load_docs():
# # # # #     base = "knowledge_base"
# # # # #     for file in os.listdir(base):
# # # # #         with open(os.path.join(base, file), "r", encoding="utf-8") as f:
# # # # #             documents.append(f.read())

# # # # # load_docs()

# # # # # # Build FAISS index
# # # # # embeddings = model.encode(documents)
# # # # # index = faiss.IndexFlatL2(embeddings.shape[1])
# # # # # index.add(embeddings)

# # # # # def retrieve_context(query: str, k=2, max_chars=400) -> str:
# # # # #     """
# # # # #     Retrieve top-k relevant knowledge chunks.
# # # # #     Returns empty string if retrieval fails.
# # # # #     """
# # # # #     if not documents:
# # # # #         return ""

# # # # #     q_emb = model.encode([query])
# # # # #     _, idxs = index.search(q_emb, k)

# # # # #     retrieved = []
# # # # #     for idx in idxs[0]:
# # # # #         retrieved.append(documents[idx][:max_chars])

# # # # #     return "\n\n".join(retrieved)


# # # # import os
# # # # import faiss
# # # # from sentence_transformers import SentenceTransformer

# # # # model = SentenceTransformer("all-MiniLM-L6-v2")
# # # # docs = []

# # # # for f in os.listdir("knowledge_base"):
# # # #     with open(os.path.join("knowledge_base", f), "r", encoding="utf-8") as file:
# # # #         docs.append(file.read())

# # # # emb = model.encode(docs)
# # # # index = faiss.IndexFlatL2(emb.shape[1])
# # # # index.add(emb)

# # # # def retrieve_context(query):
# # # #     q = model.encode([query])
# # # #     _, idx = index.search(q, 1)
# # # #     return docs[idx[0][0]]


# # # # utils/rag.py

# # # def retrieve_context(problem_text):
# # #     """
# # #     Simulate Retrieval-Augmented Generation (RAG)
# # #     Returns relevant knowledge for linear/quadratic equations
# # #     """
# # #     # In real deployment, you can use embeddings + FAISS or any vector DB
# # #     knowledge = """
# # # Linear Equation Rules:
# # # To solve ax + b = c:
# # # - Subtract b from both sides
# # # - Divide by a
# # # Always isolate the variable.

# # # Quadratic Equation Rules:
# # # For ax^2 + bx + c = 0:
# # # - Compute discriminant Δ = b^2 - 4ac
# # # - x1 = (-b + √Δ) / 2a
# # # - x2 = (-b - √Δ) / 2a

# # # Common mistakes:
# # # - Forgetting to divide fully
# # # - Sign errors
# # # - Division by zero is not allowed
# # # """
# # #     return knowledge


# # def retrieve_context(problem_text):
# #     """
# #     Mock RAG knowledge retrieval
# #     """
# #     return """Linear Equation Rules:
# # To solve ax + b = c:
# # - Subtract b from both sides
# # - Divide by a
# # Always isolate the variable.

# # Common mistakes:
# # - Forgetting to divide fully
# # - Sign errors
# # Domain rule:
# # Division by zero is not allowed."""


# def retrieve_context(problem_text):
#     # Example retrieval logic
#     knowledge_base = {
#         "linear": "Linear Equation Rules: To solve ax + b = c...",
#         "quadratic": "Quadratic Equation Rules: ax^2 + bx + c = 0..."
#     }
    
#     # Very basic matching logic
#     if "x^2" in problem_text or "^2" in problem_text:
#         return knowledge_base["quadratic"]
#     elif "x" in problem_text:
#         return knowledge_base["linear"]
#     else:
#         return "No relevant knowledge found."


# def retrieve_context(problem_text):
#     kb = {
#         "linear": "Linear Equation Rules: To solve ax + b = c...",
#         "quadratic": "Quadratic Equation Rules: ax^2 + bx + c = 0..."
#     }
#     if "^2" in problem_text or "x^2" in problem_text:
#         return kb["quadratic"]
#     elif "x" in problem_text:
#         return kb["linear"]
#     else:
#         return "No relevant knowledge found."


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

