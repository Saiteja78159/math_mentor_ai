
import os
import google.generativeai as genai

# Load API key from Streamlit secrets
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")

def call_llm(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text.strip()
