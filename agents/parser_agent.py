
# # # # # # # # # # # # import re
# # # # # # # # # # # # import json
# # # # # # # # # # # # from utils.llm import call_llm

# # # # # # # # # # # # def clean_math_text(text: str) -> str:
# # # # # # # # # # # #     """
# # # # # # # # # # # #     Remove natural language words and keep math only
# # # # # # # # # # # #     """
# # # # # # # # # # # #     text = text.lower()

# # # # # # # # # # # #     remove_words = [
# # # # # # # # # # # #         "solve", "find", "calculate", "what is",
# # # # # # # # # # # #         "please", "determine"
# # # # # # # # # # # #     ]

# # # # # # # # # # # #     for w in remove_words:
# # # # # # # # # # # #         text = text.replace(w, "")

# # # # # # # # # # # #     text = text.replace(" ", "")
# # # # # # # # # # # #     return text.strip()


# # # # # # # # # # # # def parse_input(text: str) -> dict:
# # # # # # # # # # # #     cleaned = clean_math_text(text)

# # # # # # # # # # # #     return {
# # # # # # # # # # # #         "problem_text": cleaned,
# # # # # # # # # # # #         "topic": "algebra",
# # # # # # # # # # # #         "variables": ["x"],
# # # # # # # # # # # #         "constraints": [],
# # # # # # # # # # # #         "needs_clarification": False
# # # # # # # # # # # #     }


# # # # # # # # # # # import json
# # # # # # # # # # # import re
# # # # # # # # # # # from utils.llm import call_llm

# # # # # # # # # # # def parse_input(text: str) -> dict:
# # # # # # # # # # #     prompt = f"""
# # # # # # # # # # # Return ONLY JSON:
# # # # # # # # # # # {{
# # # # # # # # # # #  "problem_text": "",
# # # # # # # # # # #  "topic": "algebra | probability | calculus | linear_algebra",
# # # # # # # # # # #  "variables": [],
# # # # # # # # # # #  "constraints": [],
# # # # # # # # # # #  "needs_clarification": false
# # # # # # # # # # # }}

# # # # # # # # # # # Input:
# # # # # # # # # # # {text}
# # # # # # # # # # # """
# # # # # # # # # # #     response = call_llm(prompt)

# # # # # # # # # # #     try:
# # # # # # # # # # #         data = json.loads(re.search(r"\{.*\}", response, re.DOTALL).group())
# # # # # # # # # # #     except:
# # # # # # # # # # #         data = fallback(text)

# # # # # # # # # # #     if re.search(r"x\^2", text):
# # # # # # # # # # #         data["topic"] = "algebra"
# # # # # # # # # # #         data["variables"] = ["x"]

# # # # # # # # # # #     return data

# # # # # # # # # # # def fallback(text):
# # # # # # # # # # #     return {
# # # # # # # # # # #         "problem_text": text,
# # # # # # # # # # #         "topic": "algebra",
# # # # # # # # # # #         "variables": ["x"],
# # # # # # # # # # #         "constraints": [],
# # # # # # # # # # #         "needs_clarification": False
# # # # # # # # # # #     }


# # # # # # # # # # # agents/parser_agent.py
# # # # # # # # # # import re

# # # # # # # # # # def parse_input(text: str) -> str:
# # # # # # # # # #     if not text:
# # # # # # # # # #         return ""

# # # # # # # # # #     text = text.lower()

# # # # # # # # # #     # Remove common command words
# # # # # # # # # #     text = re.sub(r"\b(solve|find|calculate|compute)\b", "", text)

# # # # # # # # # #     # Normalize powers
# # # # # # # # # #     text = text.replace("^", "**")
# # # # # # # # # #     text = text.replace("²", "**2")

# # # # # # # # # #     # Normalize spaces
# # # # # # # # # #     text = re.sub(r"\s+", " ", text)

# # # # # # # # # #     return text.strip()


# # # # # # # # # # # agents/parser_agent.py
# # # # # # # # # # import re

# # # # # # # # # # def parse_input(text: str) -> str:
# # # # # # # # # #     if not text:
# # # # # # # # # #         return ""

# # # # # # # # # #     text = text.lower()
# # # # # # # # # #     text = re.sub(r"\b(solve|find|calculate|compute)\b", "", text)
# # # # # # # # # #     text = text.replace("^", "**").replace("²", "**2")
# # # # # # # # # #     text = re.sub(r"\s+", " ", text)

# # # # # # # # # #     return text.strip()


# # # # # # # # # # parser_agent.py

# # # # # # # # # def parse_input(user_input: str) -> dict:
# # # # # # # # #     """
# # # # # # # # #     Parses user input and returns a dictionary with problem text.
# # # # # # # # #     Ensures solver receives a consistent format.
# # # # # # # # #     """
# # # # # # # # #     cleaned_input = user_input.lower().replace("solve", "").strip()
# # # # # # # # #     return {"problem_text": cleaned_input}


# # # # # # # # # agents/parser_agent.py

# # # # # # # # def parse_input(text):
# # # # # # # #     """
# # # # # # # #     Parses the input text (from Text, OCR, or Audio)
# # # # # # # #     Returns a dict with a clean 'problem_text'
# # # # # # # #     """
# # # # # # # #     text = text.strip().lower()
# # # # # # # #     # Remove unnecessary words like "solve"
# # # # # # # #     text = text.replace("solve", "")
# # # # # # # #     return {"problem_text": text}

# # # # # # # # agents/parser_agent.py

# # # # # # # def parse_input(user_input):
# # # # # # #     """
# # # # # # #     Parse user input and return a dictionary with problem_text key.
# # # # # # #     """
# # # # # # #     if user_input.lower().startswith("solve "):
# # # # # # #         problem_text = user_input[6:].strip()
# # # # # # #     else:
# # # # # # #         problem_text = user_input.strip()

# # # # # # #     return {"problem_text": problem_text}


# # # # # # def parse_input(text):
# # # # # #     """
# # # # # #     Simple parser for math problem.
# # # # # #     """
# # # # # #     # Just return text as a dictionary
# # # # # #     return {"problem_text": text.strip()}


# # # # # def parse_input(text):
# # # # #     """
# # # # #     Simple parser for math problem.
# # # # #     Strips unnecessary words like 'solve' at the start.
# # # # #     """
# # # # #     text = text.strip().lower()
# # # # #     if text.startswith("solve"):
# # # # #         text = text[len("solve"):].strip()
# # # # #     return {"problem_text": text}


# # # # import re

# # # # def parse_input(text):
# # # #     """
# # # #     Clean the input and prepare it for the solver.
# # # #     """
# # # #     # Lowercase and strip extra spaces
# # # #     text = text.lower().strip()
    
# # # #     # Remove the word 'solve'
# # # #     if text.startswith("solve"):
# # # #         text = text[len("solve"):].strip()
    
# # # #     # Insert '*' for implicit multiplication (like 4x -> 4*x)
# # # #     text = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', text)
    
# # # #     # Remove unsupported characters (optional)
# # # #     text = re.sub(r'[^0-9xX+\-*/^=(). ]', '', text)
    
# # # #     return {"problem_text": text}

# # # import re
# # # import json
# # # from utils.llm import call_llm

# # # def clean_math_text(text: str) -> str:
# # #     """
# # #     Remove natural language words and keep math only
# # #     """
# # #     text = text.lower()

# # #     remove_words = [
# # #         "solve", "find", "calculate", "what is",
# # #         "please", "determine"
# # #     ]

# # #     for w in remove_words:
# # #         text = text.replace(w, "")

# # #     text = text.replace(" ", "")
# # #     return text.strip()


# # # def parse_input(text: str) -> dict:
# # #     cleaned = clean_math_text(text)

# # #     return {
# # #         "problem_text": cleaned,
# # #         "topic": "algebra",
# # #         "variables": ["x"],
# # #         "constraints": [],
# # #         "needs_clarification": False
# # #     }

# # def parse_input(text: str) -> dict:
# #     cleaned = text.lower()
# #     # remove common words
# #     cleaned = re.sub(r"(solve|find|calculate|please|determine)", "", cleaned)
# #     cleaned = cleaned.replace(" ", "")

# #     return {
# #         "problem_text": cleaned,
# #         "topic": "algebra",
# #         "variables": ["x"],
# #         "constraints": [],
# #         "needs_clarification": False
# #     }


# import re  # ← add this at the top
# import math

# # =========================
# # LINEAR EQUATION SOLVER
# # ax + b = c
# # =========================
# def solve_linear_equation(equation: str):
#     equation = equation.replace(" ", "")

#     match = re.match(r"([+-]?\d*)x([+-]\d+)?=([+-]?\d+)", equation)
#     if not match:
#         return None

#     a, b, c = match.groups()

#     a = int(a) if a not in ["", "+"] else 1
#     if a == "-":
#         a = -1

#     b = int(b) if b else 0
#     c = int(c)

#     steps = []
#     steps.append(f"Given equation: {a}x + {b} = {c}")
#     steps.append(f"Subtract {b} from both sides:")
#     steps.append(f"{a}x = {c - b}")
#     steps.append(f"Divide both sides by {a}:")
#     x = (c - b) / a
#     steps.append(f"x = {x}")

#     return "\n".join(steps)


# # =========================
# # QUADRATIC EQUATION SOLVER
# # ax² + bx + c = 0
# # =========================
# def solve_quadratic_equation(equation: str):
#     equation = equation.replace(" ", "")

#     match = re.match(
#         r"([+-]?\d*)x\^2([+-]\d+)x([+-]\d+)=0",
#         equation
#     )

#     if not match:
#         return None

#     a, b, c = match.groups()

#     a = int(a) if a not in ["", "+"] else 1
#     if a == "-":
#         a = -1

#     b = int(b)
#     c = int(c)

#     steps = []
#     steps.append(f"Given equation: {a}x² + {b}x + {c} = 0")
#     steps.append("Using quadratic formula:")
#     steps.append("x = (-b ± √(b² - 4ac)) / (2a)")

#     discriminant = b**2 - 4*a*c
#     steps.append(f"Discriminant = {b}² - 4×{a}×{c} = {discriminant}")

#     if discriminant < 0:
#         steps.append("Discriminant is negative → No real solutions")
#         return "\n".join(steps)

#     sqrt_d = math.sqrt(discriminant)
#     x1 = (-b + sqrt_d) / (2*a)
#     x2 = (-b - sqrt_d) / (2*a)

#     steps.append(f"x₁ = {x1}")
#     steps.append(f"x₂ = {x2}")

#     return "\n".join(steps)


# # =========================
# # MAIN SOLVER ENTRY
# # =========================
# def solve_problem(equation: str) -> str:
#     """
#     Try quadratic first, then linear
#     """
#     quad = solve_quadratic_equation(equation)
#     if quad:
#         return quad

#     lin = solve_linear_equation(equation)
#     if lin:
#         return lin

#     return "⚠️ Only linear and quadratic equations are supported in this version."


# # =========================
# # PARSER ENTRY
# # =========================
# def parse_input(text: str) -> dict:
#     cleaned = text.lower()
#     cleaned = re.sub(r"(solve|find|calculate|please|determine)", "", cleaned)
#     cleaned = cleaned.replace(" ", "")

#     return {
#         "problem_text": cleaned,
#         "topic": "algebra",
#         "variables": ["x"],
#         "constraints": [],
#         "needs_clarification": False
#     }


def parse_input(text: str) -> dict:
    return {
        "problem_text": text,
        "topic": "algebra",
        "variables": ["x"],
        "constraints": [],
        "needs_clarification": False
    }
