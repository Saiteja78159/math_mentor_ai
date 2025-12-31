# # # # # # # # # # # # # # # # utils/ocr_utils.py
# # # # # # # # # # # # # # # import pytesseract
# # # # # # # # # # # # # # # from PIL import Image

# # # # # # # # # # # # # # # # Set Tesseract executable path
# # # # # # # # # # # # # # # pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# # # # # # # # # # # # # # # def extract_text_from_image(image_file):
# # # # # # # # # # # # # # #     """
# # # # # # # # # # # # # # #     image_file: Uploaded file from Streamlit or local path
# # # # # # # # # # # # # # #     returns: extracted text as string
# # # # # # # # # # # # # # #     """
# # # # # # # # # # # # # # #     img = Image.open(image_file)
# # # # # # # # # # # # # # #     text = pytesseract.image_to_string(img)
# # # # # # # # # # # # # # #     return text.strip()


# # # # # # # # # # # # # # # utils/ocr_utils.py


# # # # # # # # # # # # # # import pytesseract
# # # # # # # # # # # # # # from PIL import Image

# # # # # # # # # # # # # # # Set Tesseract executable path
# # # # # # # # # # # # # # pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# # # # # # # # # # # # # # def extract_text_from_image(image_file):
# # # # # # # # # # # # # #     """
# # # # # # # # # # # # # #     Extract text from an uploaded image file
# # # # # # # # # # # # # #     """
# # # # # # # # # # # # # #     img = Image.open(image_file)
# # # # # # # # # # # # # #     text = pytesseract.image_to_string(img)
# # # # # # # # # # # # # #     return clean_ocr_text(text)

# # # # # # # # # # # # # # def clean_ocr_text(text: str) -> str:
# # # # # # # # # # # # # #     """
# # # # # # # # # # # # # #     Fix common OCR mistakes for math problems
# # # # # # # # # # # # # #     """
# # # # # # # # # # # # # #     text = text.replace("x*", "x^2")    # superscript misread
# # # # # # # # # # # # # #     text = text.replace("X*", "X^2")
# # # # # # # # # # # # # #     text = text.replace("—", "-")       # long dash → minus
# # # # # # # # # # # # # #     text = text.replace("÷", "/")       # optional
# # # # # # # # # # # # # #     text = text.replace("×", "*")
# # # # # # # # # # # # # #     text = text.replace("\n", "")       # remove line breaks
# # # # # # # # # # # # # #     text = text.strip()
# # # # # # # # # # # # # #     return text


# # # # # # # # # # # # # # import pytesseract
# # # # # # # # # # # # # # from PIL import Image

# # # # # # # # # # # # # # # Set Tesseract path (Windows)
# # # # # # # # # # # # # # pytesseract.pytesseract.tesseract_cmd = (
# # # # # # # # # # # # # #     r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# # # # # # # # # # # # # # )

# # # # # # # # # # # # # # def extract_text_from_image(image: Image.Image):
# # # # # # # # # # # # # #     """
# # # # # # # # # # # # # #     Extract math text from image using OCR
# # # # # # # # # # # # # #     Returns: (text, confidence)
# # # # # # # # # # # # # #     """
# # # # # # # # # # # # # #     raw_text = pytesseract.image_to_string(image)

# # # # # # # # # # # # # #     cleaned = clean_ocr_text(raw_text)

# # # # # # # # # # # # # #     # simple confidence heuristic
# # # # # # # # # # # # # #     confidence = 0.9 if len(cleaned) > 5 else 0.4

# # # # # # # # # # # # # #     return cleaned, confidence


# # # # # # # # # # # # # # def clean_ocr_text(text: str) -> str:
# # # # # # # # # # # # # #     """
# # # # # # # # # # # # # #     Fix common OCR math errors
# # # # # # # # # # # # # #     """
# # # # # # # # # # # # # #     text = text.replace("x*", "x^2")
# # # # # # # # # # # # # #     text = text.replace("X*", "X^2")
# # # # # # # # # # # # # #     text = text.replace("—", "-")
# # # # # # # # # # # # # #     text = text.replace("×", "*")
# # # # # # # # # # # # # #     text = text.replace("÷", "/")
# # # # # # # # # # # # # #     text = text.replace("\n", "")
# # # # # # # # # # # # # #     return text.strip()


# # # # # # # # # # # # # import pytesseract
# # # # # # # # # # # # # from PIL import Image

# # # # # # # # # # # # # def extract_text_from_image(image_file):
# # # # # # # # # # # # #     img = Image.open(image_file)
# # # # # # # # # # # # #     text = pytesseract.image_to_string(img)
# # # # # # # # # # # # #     return clean_ocr_text(text)

# # # # # # # # # # # # # def clean_ocr_text(text: str) -> str:
# # # # # # # # # # # # #     text = text.replace("x*", "x^2")
# # # # # # # # # # # # #     text = text.replace("X*", "X^2")
# # # # # # # # # # # # #     text = text.replace("—", "-")
# # # # # # # # # # # # #     text = text.replace("×", "*")
# # # # # # # # # # # # #     text = text.replace("\n", "")
# # # # # # # # # # # # #     return text.strip()


# # # # # # # # # # # # # utils/ocr.py
# # # # # # # # # # # # from PIL import Image
# # # # # # # # # # # # import pytesseract

# # # # # # # # # # # # def extract_text_from_image(image_file):
# # # # # # # # # # # #     """
# # # # # # # # # # # #     Extract text from uploaded image using pytesseract OCR
# # # # # # # # # # # #     """
# # # # # # # # # # # #     image = Image.open(image_file)
# # # # # # # # # # # #     text = pytesseract.image_to_string(image)
# # # # # # # # # # # #     return text


# # # # # # # # # # # # utils/ocr.py
# # # # # # # # # # # import pytesseract
# # # # # # # # # # # from PIL import Image

# # # # # # # # # # # def extract_text_from_image(image_file):
# # # # # # # # # # #     image = Image.open(image_file)
# # # # # # # # # # #     text = pytesseract.image_to_string(image)
# # # # # # # # # # #     return text


# # # # # # # # # # from PIL import Image
# # # # # # # # # # import pytesseract

# # # # # # # # # # def extract_text_from_image(image_file):
# # # # # # # # # #     img = Image.open(image_file)
# # # # # # # # # #     text = pytesseract.image_to_string(img)
# # # # # # # # # #     return text


# # # # # # # # # from PIL import Image
# # # # # # # # # def extract_text_from_image(image_file):
# # # # # # # # #     img = Image.open(image_file)
# # # # # # # # #     text = pytesseract.image_to_string(img)
# # # # # # # # #     return text.strip()


# # # # # # # # from PIL import Image
# # # # # # # # import pytesseract

# # # # # # # # def extract_text_from_image(image_file):
# # # # # # # #     img = Image.open(image_file)
# # # # # # # #     return pytesseract.image_to_string(img).strip()



# # # # # # # import pytesseract
# # # # # # # from PIL import Image

# # # # # # # # Set Tesseract path (Windows)
# # # # # # # pytesseract.pytesseract.tesseract_cmd = (
# # # # # # #     r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# # # # # # # )

# # # # # # # def extract_text_from_image(image: Image.Image):
# # # # # # #     """
# # # # # # #     Extract math text from image using OCR
# # # # # # #     Returns: (text, confidence)
# # # # # # #     """
# # # # # # #     raw_text = pytesseract.image_to_string(image)

# # # # # # #     cleaned = clean_ocr_text(raw_text)

# # # # # # #     # simple confidence heuristic
# # # # # # #     confidence = 0.9 if len(cleaned) > 5 else 0.4

# # # # # # #     return cleaned, confidence


# # # # # # # def clean_ocr_text(text: str) -> str:
# # # # # # #     """
# # # # # # #     Fix common OCR math errors
# # # # # # #     """
# # # # # # #     text = text.replace("x*", "x^2")
# # # # # # #     text = text.replace("X*", "X^2")
# # # # # # #     text = text.replace("—", "-")
# # # # # # #     text = text.replace("×", "*")
# # # # # # #     text = text.replace("÷", "/")
# # # # # # #     text = text.replace("\n", "")
# # # # # # #     return text.strip()


# # # # # # import re
# # # # # # import pytesseract
# # # # # # from PIL import Image

# # # # # # # Set Tesseract path (Windows)
# # # # # # pytesseract.pytesseract.tesseract_cmd = (
# # # # # #     r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# # # # # # )

# # # # # # def extract_text_from_image(image: Image.Image):
# # # # # #     """
# # # # # #     Extract math text from image using OCR
# # # # # #     Returns:
# # # # # #       cleaned_text: str
# # # # # #       confidence: float (0–1)
# # # # # #       issues: list[str]
# # # # # #     """

# # # # # #     raw_text = pytesseract.image_to_string(image)

# # # # # #     cleaned_text, issues = clean_ocr_text(raw_text)

# # # # # #     # confidence scoring
# # # # # #     confidence = 1.0

# # # # # #     if len(cleaned_text) < 8:
# # # # # #         confidence -= 0.4
# # # # # #         issues.append("Very short extracted text")

# # # # # #     if "?" in cleaned_text or "*" in raw_text:
# # # # # #         confidence -= 0.3
# # # # # #         issues.append("Possible OCR symbol confusion")

# # # # # #     confidence = max(0.3, confidence)

# # # # # #     return cleaned_text, confidence, issues


# # # # # # def clean_ocr_text(text: str):
# # # # # #     """
# # # # # #     Fix common OCR math errors
# # # # # #     Returns: (cleaned_text, issues)
# # # # # #     """

# # # # # #     issues = []
# # # # # #     cleaned = text

# # # # # #     # Normalize whitespace
# # # # # #     cleaned = cleaned.replace("\n", " ")

# # # # # #     # Fix superscript confusion: x* → x^2, y* → y^2
# # # # # #     if re.search(r"[a-zA-Z]\s*\*", cleaned):
# # # # # #         cleaned = re.sub(r"([a-zA-Z])\s*\*", r"\1^2", cleaned)
# # # # # #         issues.append("Replaced '*' with '^2' for squared variable")

# # # # # #     # Common symbol fixes
# # # # # #     replacements = {
# # # # # #         "—": "-",
# # # # # #         "–": "-",
# # # # # #         "×": "*",
# # # # # #         "÷": "/",
# # # # # #         "²": "^2",
# # # # # #     }

# # # # # #     for k, v in replacements.items():
# # # # # #         if k in cleaned:
# # # # # #             cleaned = cleaned.replace(k, v)
# # # # # #             issues.append(f"Replaced '{k}' with '{v}'")

# # # # # #     cleaned = re.sub(r"\s+", " ", cleaned).strip()

# # # # # #     return cleaned, issues


# # # # # import pytesseract
# # # # # from PIL import Image
# # # # # import re

# # # # # # -------------------------
# # # # # # TESSERACT PATH (WINDOWS)
# # # # # # -------------------------
# # # # # pytesseract.pytesseract.tesseract_cmd = (
# # # # #     r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# # # # # )


# # # # # # =========================
# # # # # # MAIN OCR ENTRY
# # # # # # =========================
# # # # # def extract_text_from_image(image: Image.Image):
# # # # #     """
# # # # #     Extract math text from image using OCR
# # # # #     Returns:
# # # # #         cleaned_text (str)
# # # # #         confidence (float)
# # # # #     """

# # # # #     # OCR with better config for math
# # # # #     raw_text = pytesseract.image_to_string(
# # # # #         image,
# # # # #         config="--psm 6"
# # # # #     )

# # # # #     cleaned = normalize_math_ocr(raw_text)

# # # # #     # simple confidence heuristic
# # # # #     confidence = 0.9 if len(cleaned) >= 6 else 0.4

# # # # #     return cleaned, confidence


# # # # # # =========================
# # # # # # OCR NORMALIZATION
# # # # # # =========================
# # # # # def normalize_math_ocr(text: str) -> str:
# # # # #     """
# # # # #     Fix common OCR math mistakes robustly
# # # # #     """

# # # # #     text = text.strip()

# # # # #     # -------- BASIC SYMBOL FIXES --------
# # # # #     replacements = {
# # # # #         "×": "*",
# # # # #         "÷": "/",
# # # # #         "—": "-",
# # # # #         "–": "-",
# # # # #         "−": "-",
# # # # #         "＝": "=",
# # # # #         "﹦": "=",
# # # # #         "＋": "+",
# # # # #     }

# # # # #     for k, v in replacements.items():
# # # # #         text = text.replace(k, v)

# # # # #     # -------- REMOVE NEWLINES & SPACES --------
# # # # #     text = text.replace("\n", "")
# # # # #     text = text.replace(" ", "")

# # # # #     # -------- FIX POWERS --------
# # # # #     # x*  → x^2
# # # # #     text = re.sub(r"x\*", "x^2", text, flags=re.IGNORECASE)

# # # # #     # x² → x^2
# # # # #     text = re.sub(r"x²", "x^2", text, flags=re.IGNORECASE)

# # # # #     # x 2 → x^2
# # # # #     text = re.sub(r"x2", "x^2", text, flags=re.IGNORECASE)

# # # # #     # x^ 2 → x^2
# # # # #     text = re.sub(r"x\^\s*2", "x^2", text, flags=re.IGNORECASE)

# # # # #     # -------- FIX COMMON OCR CONFUSIONS --------
# # # # #     text = text.replace("O", "0")   # O → 0
# # # # #     text = text.replace("l", "1")   # l → 1 (rare but useful)

# # # # #     # -------- CLEAN DOUBLE OPERATORS --------
# # # # #     text = re.sub(r"\+\+", "+", text)
# # # # #     text = re.sub(r"--", "-", text)

# # # # #     return text.strip()



# # # # import pytesseract
# # # # from PIL import Image
# # # # import re

# # # # # Set Tesseract path (Windows)
# # # # pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# # # # def extract_text_from_image(image: Image.Image):
# # # #     """
# # # #     Extract math text from image using OCR
# # # #     Returns: (text, confidence)
# # # #     """
# # # #     raw_text = pytesseract.image_to_string(image)

# # # #     cleaned = clean_ocr_text(raw_text)

# # # #     # simple confidence heuristic
# # # #     confidence = 0.9 if len(cleaned) > 5 else 0.4

# # # #     return cleaned, confidence

# # # # def clean_ocr_text(text: str) -> str:
# # # #     """
# # # #     Fix common OCR math errors
# # # #     """
# # # #     text = text.lower()

# # # #     # Fix common misreads
# # # #     replacements = {
# # # #         "so1ve": "solve",
# # # #         "s0lve": "solve",
# # # #         "x*": "x^2",
# # # #         "x²": "x^2",
# # # #         "x\*": "x^2",
# # # #         "—": "-",
# # # #         "−": "-",
# # # #         "×": "*",
# # # #         "÷": "/",
# # # #         "\n": "",
# # # #         " ": ""
# # # #     }

# # # #     for k, v in replacements.items():
# # # #         text = text.replace(k, v)

# # # #     # Remove any non-math leading words like "solve", "calculate"
# # # #     text = re.sub(r"^(solve|calculate|find|please|determine)", "", text)

# # # #     return text.strip()


# # # # utils/ocr.py
# # # import easyocr
# # # from PIL import Image
# # # import numpy as np

# # # # Initialize EasyOCR reader once
# # # reader = easyocr.Reader(['en'])

# # # def extract_text_from_image(image: Image.Image):
# # #     """
# # #     Extract math text from image using EasyOCR (works on Streamlit Cloud)
# # #     Returns:
# # #         cleaned_text (str), confidence (float)
# # #     """
# # #     # Convert PIL Image to numpy array
# # #     img_array = np.array(image)

# # #     # OCR
# # #     result = reader.readtext(img_array, detail=0)  # detail=0 returns text only
# # #     raw_text = " ".join(result)

# # #     # Clean common OCR mistakes
# # #     cleaned_text = clean_ocr_text(raw_text)

# # #     # Simple confidence heuristic
# # #     confidence = 0.9 if len(cleaned_text) > 5 else 0.4

# # #     return cleaned_text, confidence


# # # def clean_ocr_text(text: str) -> str:
# # #     """
# # #     Fix common OCR math errors
# # #     """
# # #     text = text.replace("x*", "x^2")
# # #     text = text.replace("X*", "X^2")
# # #     text = text.replace("—", "-")
# # #     text = text.replace("×", "*")
# # #     text = text.replace("÷", "/")
# # #     text = text.replace("\n", "")
# # #     return text.strip()



# # # utils/ocr.py
# # import easyocr
# # from PIL import Image
# # import numpy as np
# # import re

# # # Initialize EasyOCR reader once (CPU-safe for Streamlit Cloud)
# # reader = easyocr.Reader(['en'], gpu=False)

# # def extract_text_from_image(image: Image.Image):
# #     """
# #     Extract math text from image using EasyOCR (Streamlit Cloud safe)
# #     Returns:
# #         cleaned_text (str), confidence (float)
# #     """
# #     # Convert PIL Image to numpy array
# #     img_array = np.array(image)

# #     # OCR
# #     result = reader.readtext(img_array, detail=0)
# #     raw_text = " ".join(result)

# #     # Clean OCR math mistakes
# #     cleaned_text = clean_ocr_text(raw_text)

# #     # Confidence heuristic
# #     confidence = 0.9 if "^2" in cleaned_text else 0.6

# #     return cleaned_text, confidence


# # def clean_ocr_text(text: str) -> str:
# #     """
# #     Fix common OCR math errors safely
# #     """
# #     if not text:
# #         return ""

# #     text = text.lower()
# #     text = text.replace(" ", "")

# #     # --------- POWER FIXES (CRITICAL) ----------
# #     # x² , x2 , x* → x^2
# #     text = re.sub(r"x[²2]", "x^2", text)
# #     text = text.replace("x*", "x^2")

# #     # OCR mistake: '2x+6x+8=0' when it is actually 'x^2+6x+8=0'
# #     # Fix ONLY when equation starts with 2x
# #     text = re.sub(r"^2x(?=[+\-])", "x^2", text)

# #     # --------- SYMBOL NORMALIZATION ----------
# #     text = text.replace("—", "-")
# #     text = text.replace("×", "*")
# #     text = text.replace("÷", "/")
# #     text = text.replace("\n", "")

# #     return text.strip()


# # utils/ocr.py
# import easyocr
# from PIL import Image
# import numpy as np
# import re

# reader = easyocr.Reader(['en'], gpu=False)

# def extract_text_from_image(image: Image.Image):
#     img_array = np.array(image)

#     result = reader.readtext(img_array, detail=0)
#     raw_text = " ".join(result)

#     cleaned_text = clean_ocr_text(raw_text)

#     confidence = 0.9 if len(cleaned_text) > 5 else 0.4
#     return cleaned_text, confidence


# def clean_ocr_text(text: str) -> str:
#     """
#     Fix OCR math mistakes aggressively
#     """
#     text = text.lower()

#     # Remove spaces
#     text = text.replace(" ", "")

#     # Common OCR fixes
#     text = text.replace("×", "*")
#     text = text.replace("÷", "/")
#     text = text.replace("—", "-")

#     # FIX x² misreads
#     text = re.sub(r"2x", "x^2", text)
#     text = re.sub(r"2x", "x^2", text)
#     text = re.sub(r"2\*x", "x^2", text)
#     text = re.sub(r"2x", "x^2", text)
#     text = re.sub(r"2x", "x^2", text)
#     text = re.sub(r"2x", "x^2", text)
#     text = re.sub(r"2x", "x^2", text)

#     # Fix uppercase X
#     text = text.replace("x", "x")

#     # Remove non-math characters
#     text = re.sub(r"[^0-9x^+=\-*/.]", "", text)

#     return text.strip()


# utils/ocr.py
import easyocr
from PIL import Image
import numpy as np
import re

# Initialize EasyOCR reader once
reader = easyocr.Reader(['en'])

def extract_text_from_image(image: Image.Image):
    """
    Extract math text from image using EasyOCR
    Returns:
        cleaned_text (str), confidence (float)
    """
    img_array = np.array(image)
    result = reader.readtext(img_array, detail=0)
    raw_text = " ".join(result)

    cleaned_text = clean_ocr_text(raw_text)

    # Confidence heuristic
    confidence = 0.9 if len(cleaned_text) > 5 else 0.4

    return cleaned_text, confidence


def clean_ocr_text(text: str) -> str:
    """
    Fix common OCR math errors
    """
    text = text.replace("X*", "x^2").replace("x*", "x^2")
    text = text.replace("x2", "x^2").replace("X2", "x^2")
    text = text.replace("—", "-")
    text = text.replace("×", "*").replace("÷", "/")
    text = text.replace("\n", "")
    
    # Ensure coefficients of 1 are explicit: x^2 -> 1x^2, -x -> -1x
    text = re.sub(r"(?<![\d\^])x\^2", r"1x^2", text)
    text = re.sub(r"(?<![\d])x", r"1x", text)
    text = re.sub(r"\+-", "-", text)
    
    return text.strip()
