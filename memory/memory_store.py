# # # import json
# # # import os
# # # from difflib import SequenceMatcher

# # # MEMORY_FILE = "memory/memory.json"


# # # def load_memory():
# # #     if not os.path.exists(MEMORY_FILE):
# # #         return []
# # #     with open(MEMORY_FILE, "r", encoding="utf-8") as f:
# # #         return json.load(f)


# # # def save_memory(data):
# # #     with open(MEMORY_FILE, "w", encoding="utf-8") as f:
# # #         json.dump(data, f, indent=2)


# # # def add_memory(record: dict):
# # #     memory = load_memory()
# # #     memory.append(record)
# # #     save_memory(memory)


# # # def similarity(a: str, b: str) -> float:
# # #     return SequenceMatcher(None, a, b).ratio()


# # # def retrieve_similar(problem_text: str, threshold=0.85):
# # #     memory = load_memory()
# # #     for item in memory:
# # #         if similarity(problem_text, item["parsed"]["problem_text"]) >= threshold:
# # #             return item
# # #     return None


# # import json
# # import os
# # from utils.math_normalizer import normalize_equation

# # MEMORY_FILE = "memory/memory.json"


# # def load_memory():
# #     if not os.path.exists(MEMORY_FILE):
# #         return []
# #     with open(MEMORY_FILE, "r", encoding="utf-8") as f:
# #         return json.load(f)


# # def save_memory(data):
# #     with open(MEMORY_FILE, "w", encoding="utf-8") as f:
# #         json.dump(data, f, indent=2)


# # def add_memory(record: dict):
# #     memory = load_memory()
# #     memory.append(record)
# #     save_memory(memory)


# # def retrieve_similar(problem_text: str):
# #     """
# #     Strict memory reuse:
# #     ONLY reuse if normalized equations match exactly
# #     """
# #     memory = load_memory()
# #     normalized_query = normalize_equation(problem_text)

# #     for item in memory:
# #         if item.get("normalized") == normalized_query:
# #             return item

# #     return None


# import json
# import os
# from utils.math_normalizer import normalize_math

# MEMORY_FILE = "memory/memory.json"


# def load_memory():
#     if not os.path.exists(MEMORY_FILE):
#         return []

#     with open(MEMORY_FILE, "r", encoding="utf-8") as f:
#         return json.load(f)


# def save_memory(data):
#     with open(MEMORY_FILE, "w", encoding="utf-8") as f:
#         json.dump(data, f, indent=2)


# def add_memory(record: dict):
#     memory = load_memory()
#     memory.append(record)
#     save_memory(memory)


# def retrieve_similar(problem_text: str):
#     """
#     Strict memory reuse:
#     ONLY reuse if normalized equations match exactly
#     """
#     memory = load_memory()
#     normalized_query = normalize_math(problem_text)

#     for item in memory:
#         if item.get("normalized") == normalized_query:
#             return item

#     return None


import json
import os
from utils.math_normalizer import normalize_math

MEMORY_FILE = "memory/memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_memory(data):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def add_memory(record: dict):
    memory = load_memory()
    memory.append(record)
    save_memory(memory)

def retrieve_similar(problem_text: str):
    normalized = normalize_math(problem_text)
    for item in load_memory():
        if item.get("normalized") == normalized:
            return item
    return None
