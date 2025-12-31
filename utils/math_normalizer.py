# # # # # # # # # utils/math_normalizer.py
# # # # # # # # import re

# # # # # # # # def normalize_equation(eq: str) -> str:
# # # # # # # #     """
# # # # # # # #     Normalize math equation for exact comparison
# # # # # # # #     Example:
# # # # # # # #     'Solve x^2 - 2x + 6 = 0'
# # # # # # # #     → 'x^2-2x+6=0'
# # # # # # # #     """
# # # # # # # #     eq = eq.lower()
# # # # # # # #     eq = eq.replace(" ", "")
# # # # # # # #     eq = eq.replace("−", "-")
# # # # # # # #     eq = eq.replace("×", "*")
# # # # # # # #     eq = eq.replace("÷", "/")

# # # # # # # #     # Remove non-math characters
# # # # # # # #     eq = re.sub(r"[^0-9x^=+\-*/.]", "", eq)

# # # # # # # #     return eq



# # # # # # # # utils/math_normalizer.py
# # # # # # # import re

# # # # # # # def normalize_math(text: str) -> str:
# # # # # # #     """
# # # # # # #     Normalize OCR / ASR / Text math expressions safely
# # # # # # #     """
# # # # # # #     if not text:
# # # # # # #         return ""

# # # # # # #     text = text.lower()
# # # # # # #     text = text.replace(" ", "")

# # # # # # #     # Handle unicode squared
# # # # # # #     text = re.sub(r"x[²2]", "x^2", text)

# # # # # # #     # Fix OCR case: '2x+6x+8=0' → 'x^2+6x+8=0'
# # # # # # #     text = re.sub(r"^2x(?=[+-])", "x^2", text)

# # # # # # #     # Fix inside expression
# # # # # # #     text = re.sub(r"(?<=\+)2x(?=[+-])", "+x^2", text)

# # # # # # #     # Normalize symbols
# # # # # # #     text = text.replace("—", "-")
# # # # # # #     text = text.replace("×", "*")
# # # # # # #     text = text.replace("÷", "/")

# # # # # # #     return text.strip()


# # # # # # # utils/math_normalizer.py
# # # # # # import re

# # # # # # def normalize_math(text: str) -> str:
# # # # # #     """
# # # # # #     Normalize OCR / ASR / Text math expressions
# # # # # #     """
# # # # # #     if not text:
# # # # # #         return ""

# # # # # #     text = text.lower()
# # # # # #     text = text.replace(" ", "")

# # # # # #     # Normalize unicode squared
# # # # # #     text = re.sub(r"x[²2]", "x^2", text)

# # # # # #     # Fix OCR error: 2x + 6x → x^2 + 6x
# # # # # #     text = re.sub(r"(^|[+=-])2x(?=[+-])", r"\1x^2", text)

# # # # # #     # Fix missing coefficient: -x → -1x
# # # # # #     text = re.sub(r"(?<![\dx])\-x", "-1x", text)
# # # # # #     text = re.sub(r"(?<![\dx])\+x", "+1x", text)

# # # # # #     # If starts with x^2 → 1x^2
# # # # # #     text = re.sub(r"^x\^2", "1x^2", text)

# # # # # #     # Normalize symbols
# # # # # #     text = text.replace("—", "-")
# # # # # #     text = text.replace("×", "*")
# # # # # #     text = text.replace("÷", "/")

# # # # # #     return text.strip()


# # # # # import re

# # # # # def normalize_math(text: str) -> str:
# # # # #     """
# # # # #     Normalize OCR / ASR / Text math expressions
# # # # #     """
# # # # #     if not text:
# # # # #         return ""

# # # # #     text = text.lower()
# # # # #     text = text.replace(" ", "")

# # # # #     # Normalize unicode squared (x² or x2 → x^2)
# # # # #     text = re.sub(r"x[²2]", "x^2", text)

# # # # #     # Fix OCR error: 2x + 6x → x^2 + 6x
# # # # #     text = re.sub(r"(^|[+=-])2x(?=[+-])", r"\1x^2", text)

# # # # #     # Fix missing coefficient: -x → -1x, +x → +1x
# # # # #     text = re.sub(r"(?<![\dx])\-x", "-1x", text)
# # # # #     text = re.sub(r"(?<![\dx])\+x", "+1x", text)

# # # # #     # If starts with x^2 → 1x^2
# # # # #     text = re.sub(r"^x\^2", "1x^2", text)

# # # # #     # Normalize symbols
# # # # #     text = text.replace("—", "-")
# # # # #     text = text.replace("×", "*")
# # # # #     text = text.replace("÷", "/")

# # # # #     return text.strip()


# # # # import re

# # # # def normalize_math(text: str) -> str:
# # # #     if not text:
# # # #         return ""

# # # #     text = text.lower()
# # # #     text = text.replace(" ", "")

# # # #     # remove instruction words
# # # #     text = re.sub(r"(solve|find|calculate|determine|please)", "", text)

# # # #     # normalize squared symbols
# # # #     text = re.sub(r"x[²2]", "x^2", text)

# # # #     # fix missing coefficients
# # # #     text = re.sub(r"(?<!\d)x\^2", "1x^2", text)
# # # #     text = re.sub(r"(?<!\d)([+-])x", r"\g<1>1x", text)

# # # #     # normalize operators
# # # #     text = text.replace("—", "-")
# # # #     text = text.replace("×", "*")
# # # #     text = text.replace("÷", "/")

# # # #     return text.strip()


# # # import re

# # # def normalize_math(text: str) -> str:
# # #     text = text.lower()

# # #     # remove spaces
# # #     text = text.replace(" ", "")

# # #     # normalize unicode superscripts (OCR issue)
# # #     text = text.replace("²", "^2")
# # #     text = text.replace("³", "^3")

# # #     # ensure coefficient for x^2
# # #     text = re.sub(r'(^|[+\-=])x\^2', r'\11x^2', text)

# # #     # ensure coefficient for x
# # #     text = re.sub(r'(^|[+\-=])x([^a-z^]|$)', r'\11x\2', text)

# # #     # normalize minus-x cases
# # #     text = text.replace("-x", "-1x")
# # #     text = text.replace("+x", "+1x")

# # #     # OCR common mistakes
# # #     text = text.replace("2x^", "x^2")
# # #     text = text.replace("x2", "x^2")

# # #     return text


# # # utils/math_normalizer.py
# # import re

# # def normalize_math(text: str) -> str:
# #     text = text.lower()
# #     text = text.replace(" ", "")

# #     # Normalize unicode superscripts
# #     text = text.replace("²", "^2")
# #     text = text.replace("³", "^3")

# #     # Add coefficient to x^2 → 1x^2
# #     text = re.sub(r'(?<!\d)x\^2', '1x^2', text)

# #     # Add coefficient to x → 1x
# #     text = re.sub(r'(?<=[+=\-])x', '1x', text)
# #     text = re.sub(r'^x', '1x', text)

# #     return text


# # utils/math_normalizer.py
# import re

# def normalize_math(text: str) -> str:
#     text = text.lower()
#     text = text.replace(" ", "")

#     # Normalize unicode superscripts
#     text = text.replace("²", "^2")
#     text = text.replace("³", "^3")

#     # -----------------------------
#     # Fix implicit coefficients
#     # -----------------------------

#     # x^2 → 1x^2
#     text = re.sub(r'(?<!\d)x\^2', '1x^2', text)

#     # +x → +1x
#     text = re.sub(r'\+x', '+1x', text)

#     # -x → -1x
#     text = re.sub(r'\-x', '-1x', text)

#     # x at start → 1x
#     text = re.sub(r'^x', '1x', text)

#     return text


# utils/math_normalizer.py
import re

def normalize_math(text: str) -> str:
    text = text.lower()
    text = text.replace(" ", "")

    # Normalize unicode superscripts
    text = text.replace("²", "^2")
    text = text.replace("³", "^3")

    # x^2 → 1x^2
    text = re.sub(r'(?<!\d)x\^2', '1x^2', text)

    # FIX: -x → -1x , +x → +1x
    text = re.sub(r'(?<=[+\-=])x', '1x', text)

    # x at start → 1x
    text = re.sub(r'^x', '1x', text)

    return text
