

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
