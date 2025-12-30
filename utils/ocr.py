# # # utils/ocr_utils.py
# # import pytesseract
# # from PIL import Image

# # # Set Tesseract executable path
# # pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# # def extract_text_from_image(image_file):
# #     """
# #     image_file: Uploaded file from Streamlit or local path
# #     returns: extracted text as string
# #     """
# #     img = Image.open(image_file)
# #     text = pytesseract.image_to_string(img)
# #     return text.strip()


# # utils/ocr_utils.py


# import pytesseract
# from PIL import Image

# # Set Tesseract executable path
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# def extract_text_from_image(image_file):
#     """
#     Extract text from an uploaded image file
#     """
#     img = Image.open(image_file)
#     text = pytesseract.image_to_string(img)
#     return clean_ocr_text(text)

# def clean_ocr_text(text: str) -> str:
#     """
#     Fix common OCR mistakes for math problems
#     """
#     text = text.replace("x*", "x^2")    # superscript misread
#     text = text.replace("X*", "X^2")
#     text = text.replace("—", "-")       # long dash → minus
#     text = text.replace("÷", "/")       # optional
#     text = text.replace("×", "*")
#     text = text.replace("\n", "")       # remove line breaks
#     text = text.strip()
#     return text


# import pytesseract
# from PIL import Image

# # Set Tesseract path (Windows)
# pytesseract.pytesseract.tesseract_cmd = (
#     r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# )

# def extract_text_from_image(image: Image.Image):
#     """
#     Extract math text from image using OCR
#     Returns: (text, confidence)
#     """
#     raw_text = pytesseract.image_to_string(image)

#     cleaned = clean_ocr_text(raw_text)

#     # simple confidence heuristic
#     confidence = 0.9 if len(cleaned) > 5 else 0.4

#     return cleaned, confidence


# def clean_ocr_text(text: str) -> str:
#     """
#     Fix common OCR math errors
#     """
#     text = text.replace("x*", "x^2")
#     text = text.replace("X*", "X^2")
#     text = text.replace("—", "-")
#     text = text.replace("×", "*")
#     text = text.replace("÷", "/")
#     text = text.replace("\n", "")
#     return text.strip()


import pytesseract
from PIL import Image

def extract_text_from_image(image_file):
    img = Image.open(image_file)
    text = pytesseract.image_to_string(img)
    return clean_ocr_text(text)

def clean_ocr_text(text: str) -> str:
    text = text.replace("x*", "x^2")
    text = text.replace("X*", "X^2")
    text = text.replace("—", "-")
    text = text.replace("×", "*")
    text = text.replace("\n", "")
    return text.strip()
