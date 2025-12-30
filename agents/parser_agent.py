
# import re
# import json
# from utils.llm import call_llm

# def clean_math_text(text: str) -> str:
#     """
#     Remove natural language words and keep math only
#     """
#     text = text.lower()

#     remove_words = [
#         "solve", "find", "calculate", "what is",
#         "please", "determine"
#     ]

#     for w in remove_words:
#         text = text.replace(w, "")

#     text = text.replace(" ", "")
#     return text.strip()


# def parse_input(text: str) -> dict:
#     cleaned = clean_math_text(text)

#     return {
#         "problem_text": cleaned,
#         "topic": "algebra",
#         "variables": ["x"],
#         "constraints": [],
#         "needs_clarification": False
#     }


import json
import re
from utils.llm import call_llm

def parse_input(text: str) -> dict:
    prompt = f"""
Return ONLY JSON:
{{
 "problem_text": "",
 "topic": "algebra | probability | calculus | linear_algebra",
 "variables": [],
 "constraints": [],
 "needs_clarification": false
}}

Input:
{text}
"""
    response = call_llm(prompt)

    try:
        data = json.loads(re.search(r"\{.*\}", response, re.DOTALL).group())
    except:
        data = fallback(text)

    if re.search(r"x\^2", text):
        data["topic"] = "algebra"
        data["variables"] = ["x"]

    return data

def fallback(text):
    return {
        "problem_text": text,
        "topic": "algebra",
        "variables": ["x"],
        "constraints": [],
        "needs_clarification": False
    }
