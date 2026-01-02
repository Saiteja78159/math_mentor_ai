

import re

def normalize_math(text: str) -> str:
    text = text.lower()
    text = text.replace(" ", "")

    # Normalize unicode superscripts
    text = text.replace("²", "^2")
    text = text.replace("³", "^3")

    # Add coefficient 1 to x^2 if missing
    text = re.sub(r'(?<!\d)x\^2', '1x^2', text)

    # Add coefficient 1 to standalone x
    text = re.sub(r'^x', '1x', text)                 # x → 1x
    text = re.sub(r'([+-])x', r'\g<1>1x', text)      # +x / -x → +1x / -1x

    return text
