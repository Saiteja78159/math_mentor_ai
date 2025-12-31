# # # import subprocess

# # # OLLAMA_PATH = r"C:\Users\ganes\AppData\Local\Programs\Ollama\ollama.exe"

# # # def call_llm(prompt: str) -> str:
# # #     result = subprocess.run(
# # #         [
# # #             OLLAMA_PATH,
# # #             "run",
# # #             "phi3:mini",
# # #             "--num-predict",
# # #             "256"          # LIMIT TOKENS → prevents crash
# # #         ],
# # #         input=prompt,
# # #         text=True,
# # #         encoding="utf-8",
# # #         errors="ignore",
# # #         capture_output=True
# # #     )

# # #     if result.returncode != 0:
# # #         return "⚠️ LLM could not generate answer due to memory limits."

# # #     return result.stdout.strip()


# # def call_llm(prompt: str) -> str:
# #     """
# #     Streamlit Cloud safe fallback.
# #     Used only for parsing & routing.
# #     """
# #     return """
# # {
# #   "problem_text": "Solve the given math problem",
# #   "topic": "algebra",
# #   "variables": ["x"],
# #   "constraints": [],
# #   "needs_clarification": false
# # }
# # """


# import subprocess

# OLLAMA_PATH = r"C:\Users\ganes\AppData\Local\Programs\Ollama\ollama.exe"

# def call_llm(prompt: str) -> str:
#     result = subprocess.run(
#         [
#             OLLAMA_PATH,
#             "run",
#             "phi3:mini",
#             "--num-predict",
#             "256"          # LIMIT TOKENS → prevents crash
#         ],
#         input=prompt,
#         text=True,
#         encoding="utf-8",
#         errors="ignore",
#         capture_output=True
#     )

#     if result.returncode != 0:
#         return "⚠️ LLM could not generate answer due to memory limits."

#     return result.stdout.strip()


# import os
# import google.generativeai as genai

# # Configure Gemini using environment variable
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# # Load Gemini model
# model = genai.GenerativeModel("gemini-1.5-flash")

# def call_llm(prompt: str) -> str:
#     """
#     Call Gemini LLM safely for cloud deployment
#     """
#     response = model.generate_content(prompt)
#     return response.text.strip()


import os
import google.generativeai as genai

# Load API key from Streamlit secrets
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")

def call_llm(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text.strip()

