import json
import os
from difflib import SequenceMatcher

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


def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


def retrieve_similar(problem_text: str, threshold=0.85):
    memory = load_memory()
    for item in memory:
        if similarity(problem_text, item["parsed"]["problem_text"]) >= threshold:
            return item
    return None
