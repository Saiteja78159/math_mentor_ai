import re
import math


# =========================
# LINEAR EQUATION SOLVER
# ax + b = c
# =========================
def solve_linear_equation(equation: str):
    equation = equation.replace(" ", "")

    match = re.match(r"([+-]?\d*)x([+-]\d+)?=([+-]?\d+)", equation)
    if not match:
        return None

    a, b, c = match.groups()

    a = int(a) if a not in ["", "+"] else 1
    if a == "-":
        a = -1

    b = int(b) if b else 0
    c = int(c)

    steps = []
    steps.append(f"Given equation: {a}x + {b} = {c}")
    steps.append(f"Subtract {b} from both sides:")
    steps.append(f"{a}x = {c - b}")
    steps.append(f"Divide both sides by {a}:")
    x = (c - b) / a
    steps.append(f"x = {x}")

    return "\n".join(steps)


# =========================
# QUADRATIC EQUATION SOLVER
# ax² + bx + c = 0
# =========================
def solve_quadratic_equation(equation: str):
    equation = equation.replace(" ", "")

    match = re.match(
        r"([+-]?\d*)x\^2([+-]\d+)x([+-]\d+)=0",
        equation
    )

    if not match:
        return None

    a, b, c = match.groups()

    a = int(a) if a not in ["", "+"] else 1
    if a == "-":
        a = -1

    b = int(b)
    c = int(c)

    steps = []
    steps.append(f"Given equation: {a}x² + {b}x + {c} = 0")
    steps.append("Using quadratic formula:")
    steps.append("x = (-b ± √(b² - 4ac)) / (2a)")

    discriminant = b**2 - 4*a*c
    steps.append(f"Discriminant = {b}² - 4×{a}×{c} = {discriminant}")

    if discriminant < 0:
        steps.append("Discriminant is negative → No real solutions")
        return "\n".join(steps)

    sqrt_d = math.sqrt(discriminant)
    x1 = (-b + sqrt_d) / (2*a)
    x2 = (-b - sqrt_d) / (2*a)

    steps.append(f"x₁ = {x1}")
    steps.append(f"x₂ = {x2}")

    return "\n".join(steps)


# =========================
# MAIN SOLVER ENTRY
# =========================
def solve_problem(equation: str) -> str:
    """
    Try quadratic first, then linear
    """
    quad = solve_quadratic_equation(equation)
    if quad:
        return quad

    lin = solve_linear_equation(equation)
    if lin:
        return lin

    return "⚠️ Only linear and quadratic equations are supported in this version."
