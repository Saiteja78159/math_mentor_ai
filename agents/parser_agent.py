
import re
import json
from utils.llm import call_llm

def clean_math_text(text: str) -> str:
    """
    Remove natural language words and keep math only
    """
    text = text.lower()

    remove_words = [
        "solve", "find", "calculate", "what is",
        "please", "determine"
    ]

    for w in remove_words:
        text = text.replace(w, "")

    text = text.replace(" ", "")
    return text.strip()


def parse_input(text: str) -> dict:
    cleaned = clean_math_text(text)

    return {
        "problem_text": cleaned,
        "topic": "algebra",
        "variables": ["x"],
        "constraints": [],
        "needs_clarification": False
    }
