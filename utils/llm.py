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


def call_llm(prompt: str) -> str:
    """
    Streamlit Cloud safe fallback.
    Used only for parsing & routing.
    """
    return """
{
  "problem_text": "Solve the given math problem",
  "topic": "algebra",
  "variables": ["x"],
  "constraints": [],
  "needs_clarification": false
}
"""
