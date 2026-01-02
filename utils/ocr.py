

# utils/ocr.py
import easyocr
from PIL import Image
import numpy as np
import re

reader = easyocr.Reader(['en'], gpu=False)

def extract_text_from_image(image: Image.Image):
    img_array = np.array(image)
    result = reader.readtext(img_array, detail=0)
    raw_text = " ".join(result)

    cleaned = clean_ocr_text(raw_text)
    confidence = estimate_confidence(cleaned)

    return cleaned, confidence


def clean_ocr_text(text: str) -> str:
    text = text.lower()
    text = text.replace(" ", "")

    # Normalize symbols ONLY
    text = text.replace("—", "-")
    text = text.replace("×", "x")
    text = text.replace("÷", "/")
    text = text.replace("\n", "")

    # Superscript fixes (representation only)
    text = text.replace("x²", "x^2")
    text = text.replace("x2", "x^2")
    text = text.replace("x*", "x^2")
    text = text.replace("xˆ2", "x^2")

    # Remove junk characters
    text = re.sub(r'[^0-9x\^+=\-*/().]', '', text)

    return text.strip()


def estimate_confidence(text: str) -> float:
    if "x^2" in text:
        return 0.9
    if "x" in text:
        return 0.7
    return 0.4
