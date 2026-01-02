

import re
import math

# =========================
# LINEAR SOLVER
# ax + b = c
# =========================
def solve_linear_equation(equation: str):
    match = re.match(r"([+-]?\d+)x([+-]\d+)=([+-]?\d+)", equation)
    if not match:
        return None

    a, b, c = map(int, match.groups())
    x = (c - b) / a

    return (
        f"Given equation: {a}x + {b} = {c}\n"
        f"{a}x = {c-b}\n"
        f"x = {x}"
    )


# =========================
# QUADRATIC SOLVER
# ax² + bx + c = 0
# =========================
def solve_quadratic_equation(equation: str):
    match = re.match(
        r"([+-]?\d+)x\^2([+-]\d+)x([+-]\d+)=0",
        equation
    )
    if not match:
        return None

    a, b, c = map(int, match.groups())

    steps = []
    steps.append(f"Given equation: {a}x² + {b}x + {c} = 0")
    steps.append("Using quadratic formula:")
    steps.append("x = (-b ± √(b² - 4ac)) / (2a)")

    d = b*b - 4*a*c
    steps.append(f"Discriminant = {d}")

    if d < 0:
        real = -b / (2*a)
        imag = math.sqrt(abs(d)) / (2*a)
        steps.append("Complex roots:")
        steps.append(f"x₁ = {real} + {imag}i")
        steps.append(f"x₂ = {real} - {imag}i")
        return "\n".join(steps)

    sqrt_d = math.sqrt(d)
    x1 = (-b + sqrt_d) / (2*a)
    x2 = (-b - sqrt_d) / (2*a)

    steps.append(f"x₁ = {x1}")
    steps.append(f"x₂ = {x2}")

    return "\n".join(steps)


# =========================
# MAIN ENTRY
# =========================
def solve_problem(equation: str) -> str:
    quad = solve_quadratic_equation(equation)
    if quad:
        return quad

    lin = solve_linear_equation(equation)
    if lin:
        return lin

    return "⚠️ Only linear and quadratic equations are supported."
