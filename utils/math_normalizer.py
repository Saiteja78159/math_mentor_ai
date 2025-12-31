# utils/math_normalizer.py
import re

def normalize_equation(eq: str) -> str:
    """
    Normalize math equation for exact comparison
    Example:
    'Solve x^2 - 2x + 6 = 0'
    → 'x^2-2x+6=0'
    """
    eq = eq.lower()
    eq = eq.replace(" ", "")
    eq = eq.replace("−", "-")
    eq = eq.replace("×", "*")
    eq = eq.replace("÷", "/")

    # Remove non-math characters
    eq = re.sub(r"[^0-9x^=+\-*/.]", "", eq)

    return eq
