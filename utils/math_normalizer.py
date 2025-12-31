# # # # utils/math_normalizer.py
# # # import re

# # # def normalize_equation(eq: str) -> str:
# # #     """
# # #     Normalize math equation for exact comparison
# # #     Example:
# # #     'Solve x^2 - 2x + 6 = 0'
# # #     → 'x^2-2x+6=0'
# # #     """
# # #     eq = eq.lower()
# # #     eq = eq.replace(" ", "")
# # #     eq = eq.replace("−", "-")
# # #     eq = eq.replace("×", "*")
# # #     eq = eq.replace("÷", "/")

# # #     # Remove non-math characters
# # #     eq = re.sub(r"[^0-9x^=+\-*/.]", "", eq)

# # #     return eq



# # # utils/math_normalizer.py
# # import re

# # def normalize_math(text: str) -> str:
# #     """
# #     Normalize OCR / ASR / Text math expressions safely
# #     """
# #     if not text:
# #         return ""

# #     text = text.lower()
# #     text = text.replace(" ", "")

# #     # Handle unicode squared
# #     text = re.sub(r"x[²2]", "x^2", text)

# #     # Fix OCR case: '2x+6x+8=0' → 'x^2+6x+8=0'
# #     text = re.sub(r"^2x(?=[+-])", "x^2", text)

# #     # Fix inside expression
# #     text = re.sub(r"(?<=\+)2x(?=[+-])", "+x^2", text)

# #     # Normalize symbols
# #     text = text.replace("—", "-")
# #     text = text.replace("×", "*")
# #     text = text.replace("÷", "/")

# #     return text.strip()


# # utils/math_normalizer.py
# import re

# def normalize_math(text: str) -> str:
#     """
#     Normalize OCR / ASR / Text math expressions
#     """
#     if not text:
#         return ""

#     text = text.lower()
#     text = text.replace(" ", "")

#     # Normalize unicode squared
#     text = re.sub(r"x[²2]", "x^2", text)

#     # Fix OCR error: 2x + 6x → x^2 + 6x
#     text = re.sub(r"(^|[+=-])2x(?=[+-])", r"\1x^2", text)

#     # Fix missing coefficient: -x → -1x
#     text = re.sub(r"(?<![\dx])\-x", "-1x", text)
#     text = re.sub(r"(?<![\dx])\+x", "+1x", text)

#     # If starts with x^2 → 1x^2
#     text = re.sub(r"^x\^2", "1x^2", text)

#     # Normalize symbols
#     text = text.replace("—", "-")
#     text = text.replace("×", "*")
#     text = text.replace("÷", "/")

#     return text.strip()


import re

def normalize_math(text: str) -> str:
    """
    Normalize OCR / ASR / Text math expressions
    """
    if not text:
        return ""

    text = text.lower()
    text = text.replace(" ", "")

    # Normalize unicode squared (x² or x2 → x^2)
    text = re.sub(r"x[²2]", "x^2", text)

    # Fix OCR error: 2x + 6x → x^2 + 6x
    text = re.sub(r"(^|[+=-])2x(?=[+-])", r"\1x^2", text)

    # Fix missing coefficient: -x → -1x, +x → +1x
    text = re.sub(r"(?<![\dx])\-x", "-1x", text)
    text = re.sub(r"(?<![\dx])\+x", "+1x", text)

    # If starts with x^2 → 1x^2
    text = re.sub(r"^x\^2", "1x^2", text)

    # Normalize symbols
    text = text.replace("—", "-")
    text = text.replace("×", "*")
    text = text.replace("÷", "/")

    return text.strip()
