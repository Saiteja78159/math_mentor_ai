# # # # # # # # # # # # import re
# # # # # # # # # # # # import math


# # # # # # # # # # # # # =========================
# # # # # # # # # # # # # LINEAR EQUATION SOLVER
# # # # # # # # # # # # # ax + b = c
# # # # # # # # # # # # # =========================
# # # # # # # # # # # # def solve_linear_equation(equation: str):
# # # # # # # # # # # #     equation = equation.replace(" ", "")

# # # # # # # # # # # #     match = re.match(r"([+-]?\d*)x([+-]\d+)?=([+-]?\d+)", equation)
# # # # # # # # # # # #     if not match:
# # # # # # # # # # # #         return None

# # # # # # # # # # # #     a, b, c = match.groups()

# # # # # # # # # # # #     a = int(a) if a not in ["", "+"] else 1
# # # # # # # # # # # #     if a == "-":
# # # # # # # # # # # #         a = -1

# # # # # # # # # # # #     b = int(b) if b else 0
# # # # # # # # # # # #     c = int(c)

# # # # # # # # # # # #     steps = []
# # # # # # # # # # # #     steps.append(f"Given equation: {a}x + {b} = {c}")
# # # # # # # # # # # #     steps.append(f"Subtract {b} from both sides:")
# # # # # # # # # # # #     steps.append(f"{a}x = {c - b}")
# # # # # # # # # # # #     steps.append(f"Divide both sides by {a}:")
# # # # # # # # # # # #     x = (c - b) / a
# # # # # # # # # # # #     steps.append(f"x = {x}")

# # # # # # # # # # # #     return "\n".join(steps)


# # # # # # # # # # # # # =========================
# # # # # # # # # # # # # QUADRATIC EQUATION SOLVER
# # # # # # # # # # # # # ax² + bx + c = 0
# # # # # # # # # # # # # =========================
# # # # # # # # # # # # def solve_quadratic_equation(equation: str):
# # # # # # # # # # # #     equation = equation.replace(" ", "")

# # # # # # # # # # # #     match = re.match(
# # # # # # # # # # # #         r"([+-]?\d*)x\^2([+-]\d+)x([+-]\d+)=0",
# # # # # # # # # # # #         equation
# # # # # # # # # # # #     )

# # # # # # # # # # # #     if not match:
# # # # # # # # # # # #         return None

# # # # # # # # # # # #     a, b, c = match.groups()

# # # # # # # # # # # #     a = int(a) if a not in ["", "+"] else 1
# # # # # # # # # # # #     if a == "-":
# # # # # # # # # # # #         a = -1

# # # # # # # # # # # #     b = int(b)
# # # # # # # # # # # #     c = int(c)

# # # # # # # # # # # #     steps = []
# # # # # # # # # # # #     steps.append(f"Given equation: {a}x² + {b}x + {c} = 0")
# # # # # # # # # # # #     steps.append("Using quadratic formula:")
# # # # # # # # # # # #     steps.append("x = (-b ± √(b² - 4ac)) / (2a)")

# # # # # # # # # # # #     discriminant = b**2 - 4*a*c
# # # # # # # # # # # #     steps.append(f"Discriminant = {b}² - 4×{a}×{c} = {discriminant}")

# # # # # # # # # # # #     if discriminant < 0:
# # # # # # # # # # # #         steps.append("Discriminant is negative → No real solutions")
# # # # # # # # # # # #         return "\n".join(steps)

# # # # # # # # # # # #     sqrt_d = math.sqrt(discriminant)
# # # # # # # # # # # #     x1 = (-b + sqrt_d) / (2*a)
# # # # # # # # # # # #     x2 = (-b - sqrt_d) / (2*a)

# # # # # # # # # # # #     steps.append(f"x₁ = {x1}")
# # # # # # # # # # # #     steps.append(f"x₂ = {x2}")

# # # # # # # # # # # #     return "\n".join(steps)


# # # # # # # # # # # # # =========================
# # # # # # # # # # # # # MAIN SOLVER ENTRY
# # # # # # # # # # # # # =========================
# # # # # # # # # # # # def solve_problem(equation: str) -> str:
# # # # # # # # # # # #     """
# # # # # # # # # # # #     Try quadratic first, then linear
# # # # # # # # # # # #     """
# # # # # # # # # # # #     quad = solve_quadratic_equation(equation)
# # # # # # # # # # # #     if quad:
# # # # # # # # # # # #         return quad

# # # # # # # # # # # #     lin = solve_linear_equation(equation)
# # # # # # # # # # # #     if lin:
# # # # # # # # # # # #         return lin

# # # # # # # # # # # #     return "⚠️ Only linear and quadratic equations are supported in this version."



# # # # # # # # # # # # import re
# # # # # # # # # # # # import math

# # # # # # # # # # # # def solve_quadratic(eq: str):
# # # # # # # # # # # #     m = re.search(r"([+-]?\d*)x\^2([+-]?\d*)x([+-]?\d+)=?0", eq.replace(" ", ""))
# # # # # # # # # # # #     if not m:
# # # # # # # # # # # #         return None

# # # # # # # # # # # #     a, b, c = m.groups()
# # # # # # # # # # # #     a = int(a) if a not in ["", "+"] else 1
# # # # # # # # # # # #     b = int(b) if b not in ["", "+"] else 1
# # # # # # # # # # # #     c = int(c)

# # # # # # # # # # # #     d = b*b - 4*a*c
# # # # # # # # # # # #     if d < 0:
# # # # # # # # # # # #         return "No real roots"

# # # # # # # # # # # #     r = math.sqrt(d)
# # # # # # # # # # # #     return f"x₁ = {(-b+r)/(2*a)}, x₂ = {(-b-r)/(2*a)}"

# # # # # # # # # # # # def solve_linear(eq: str):
# # # # # # # # # # # #     m = re.search(r"([+-]?\d*)x([+-]\d+)?=([+-]?\d+)", eq.replace(" ", ""))
# # # # # # # # # # # #     if not m:
# # # # # # # # # # # #         return None

# # # # # # # # # # # #     a, b, c = m.groups()
# # # # # # # # # # # #     a = int(a) if a not in ["", "+"] else 1
# # # # # # # # # # # #     b = int(b) if b else 0
# # # # # # # # # # # #     c = int(c)
# # # # # # # # # # # #     return f"x = {(c - b) / a}"

# # # # # # # # # # # # def solve_problem(text: str):
# # # # # # # # # # # #     return solve_quadratic(text) or solve_linear(text) or "Unsupported problem"


# # # # # # # # # # # # agents/solver_agent.py
# # # # # # # # # # # import sympy as sp

# # # # # # # # # # # def solve_math_problem(problem: str) -> str:
# # # # # # # # # # #     x = sp.symbols('x')

# # # # # # # # # # #     try:
# # # # # # # # # # #         lhs, rhs = problem.split("=")
# # # # # # # # # # #         eq = sp.Eq(sp.sympify(lhs), sp.sympify(rhs))
# # # # # # # # # # #         sol = sp.solve(eq, x)

# # # # # # # # # # #         if len(sol) == 2:
# # # # # # # # # # #             return f"x₁ = {sol[0]}, x₂ = {sol[1]}"
# # # # # # # # # # #         return f"x = {sol[0]}"

# # # # # # # # # # #     except Exception:
# # # # # # # # # # #         return "Unsupported problem"



# # # # # # # # # # # agents/solver_agent.py
# # # # # # # # # # import sympy as sp

# # # # # # # # # # def solve_problem(problem: str) -> str:
# # # # # # # # # #     x = sp.symbols('x')

# # # # # # # # # #     try:
# # # # # # # # # #         # Ensure equation format
# # # # # # # # # #         if "=" not in problem:
# # # # # # # # # #             return "Unsupported problem"

# # # # # # # # # #         lhs, rhs = problem.split("=")
# # # # # # # # # #         equation = sp.Eq(sp.sympify(lhs), sp.sympify(rhs))

# # # # # # # # # #         solutions = sp.solve(equation, x)

# # # # # # # # # #         if not solutions:
# # # # # # # # # #             return "No solution found"

# # # # # # # # # #         if len(solutions) == 1:
# # # # # # # # # #             return f"x = {solutions[0]}"

# # # # # # # # # #         return f"x₁ = {solutions[0]}, x₂ = {solutions[1]}"

# # # # # # # # # #     except Exception:
# # # # # # # # # #         return "Unsupported problem"



# # # # # # # # # import re
# # # # # # # # # import math

# # # # # # # # # # ---------------- CLEAN INPUT ----------------
# # # # # # # # # def normalize_equation(text: str) -> str:
# # # # # # # # #     text = text.lower()
# # # # # # # # #     text = re.sub(r"(solve|find|calculate|what is|please)", "", text)
# # # # # # # # #     text = text.replace(" ", "")
# # # # # # # # #     return text


# # # # # # # # # # ---------------- LINEAR SOLVER ----------------
# # # # # # # # # def solve_linear(equation: str):
# # # # # # # # #     match = re.fullmatch(r"([+-]?\d*)x([+-]\d+)?=([+-]?\d+)", equation)
# # # # # # # # #     if not match:
# # # # # # # # #         return None

# # # # # # # # #     a, b, c = match.groups()

# # # # # # # # #     a = int(a) if a not in ["", "+"] else 1
# # # # # # # # #     if a == "-":
# # # # # # # # #         a = -1

# # # # # # # # #     b = int(b) if b else 0
# # # # # # # # #     c = int(c)

# # # # # # # # #     x = (c - b) / a

# # # # # # # # #     return f"""
# # # # # # # # # Given equation: {a}x + {b} = {c}
# # # # # # # # # Subtract {b} from both sides:
# # # # # # # # # {a}x = {c - b}
# # # # # # # # # Divide both sides by {a}:
# # # # # # # # # x = {x}
# # # # # # # # # """.strip()


# # # # # # # # # # ---------------- QUADRATIC SOLVER ----------------
# # # # # # # # # def solve_quadratic(equation: str):
# # # # # # # # #     match = re.fullmatch(
# # # # # # # # #         r"([+-]?\d*)x\^2([+-]?\d*)x([+-]?\d+)=0",
# # # # # # # # #         equation
# # # # # # # # #     )
# # # # # # # # #     if not match:
# # # # # # # # #         return None

# # # # # # # # #     a, b, c = match.groups()

# # # # # # # # #     a = int(a) if a not in ["", "+"] else 1
# # # # # # # # #     if a == "-":
# # # # # # # # #         a = -1

# # # # # # # # #     b = int(b) if b not in ["", "+"] else 1
# # # # # # # # #     c = int(c)

# # # # # # # # #     d = b**2 - 4*a*c

# # # # # # # # #     if d < 0:
# # # # # # # # #         return "No real solutions (discriminant < 0)"

# # # # # # # # #     sqrt_d = math.sqrt(d)
# # # # # # # # #     x1 = (-b + sqrt_d) / (2*a)
# # # # # # # # #     x2 = (-b - sqrt_d) / (2*a)

# # # # # # # # #     return f"""
# # # # # # # # # Given equation: {a}x² + {b}x + {c} = 0
# # # # # # # # # Discriminant = {d}

# # # # # # # # # x₁ = {x1}
# # # # # # # # # x₂ = {x2}
# # # # # # # # # """.strip()


# # # # # # # # # # ---------------- MAIN ENTRY ----------------
# # # # # # # # # def solve_problem(parsed: dict) -> str:
# # # # # # # # #     equation = normalize_equation(parsed["problem_text"])

# # # # # # # # #     quad = solve_quadratic(equation)
# # # # # # # # #     if quad:
# # # # # # # # #         return quad

# # # # # # # # #     linear = solve_linear(equation)
# # # # # # # # #     if linear:
# # # # # # # # #         return linear

# # # # # # # # #     return "⚠️ Unsupported problem format"


# # # # # # # # # solver_agent.py
# # # # # # # # import re
# # # # # # # # import math

# # # # # # # # def normalize_equation(equation: str) -> str:
# # # # # # # #     """
# # # # # # # #     Cleans and standardizes the equation string.
# # # # # # # #     """
# # # # # # # #     equation = equation.replace(" ", "")
# # # # # # # #     equation = equation.replace("^", "**")
# # # # # # # #     return equation

# # # # # # # # def solve_problem(parsed: dict) -> dict:
# # # # # # # #     """
# # # # # # # #     Solves linear and quadratic equations.
# # # # # # # #     Returns solution dict with x values.
# # # # # # # #     """
# # # # # # # #     equation = parsed["problem_text"]
# # # # # # # #     equation = normalize_equation(equation)

# # # # # # # #     # Quadratic: ax^2 + bx + c = 0
# # # # # # # #     match = re.match(r"([+-]?\d*)x\*\*2([+-]\d*)x([+-]\d+)=?0", equation)
# # # # # # # #     if match:
# # # # # # # #         a = int(match.group(1)) if match.group(1) not in ["", "+", "-"] else int(match.group(1)+"1" if match.group(1) else "1")
# # # # # # # #         b = int(match.group(2))
# # # # # # # #         c = int(match.group(3))
# # # # # # # #         discriminant = b**2 - 4*a*c
# # # # # # # #         if discriminant < 0:
# # # # # # # #             return {"solution": "No real roots"}
# # # # # # # #         x1 = (-b + math.sqrt(discriminant)) / (2*a)
# # # # # # # #         x2 = (-b - math.sqrt(discriminant)) / (2*a)
# # # # # # # #         return {"solution": [x1, x2]}
    
# # # # # # # #     # Linear: ax + b = 0
# # # # # # # #     match = re.match(r"([+-]?\d*)x([+-]\d+)=?0", equation)
# # # # # # # #     if match:
# # # # # # # #         a = int(match.group(1)) if match.group(1) not in ["", "+", "-"] else int(match.group(1)+"1" if match.group(1) else "1")
# # # # # # # #         b = int(match.group(2))
# # # # # # # #         x = -b / a
# # # # # # # #         return {"solution": [x]}

# # # # # # # #     return {"solution": "Unsupported problem"}


# # # # # # # # agents/solver_agent.py
# # # # # # # import re

# # # # # # # def normalize_equation(text):
# # # # # # #     """Clean and normalize the equation text"""
# # # # # # #     return text.replace(" ", "").replace("solve", "").lower()

# # # # # # # def solve_problem(parsed):
# # # # # # #     """
# # # # # # #     Solves linear and quadratic equations.
# # # # # # #     Returns both solution and step-by-step explanation.
# # # # # # #     """
# # # # # # #     problem_text = parsed["problem_text"]
# # # # # # #     eq_text = normalize_equation(problem_text)
    
# # # # # # #     # Quadratic equation: x^2 + bx + c = 0
# # # # # # #     match = re.match(r"x\^2([+-]\d+)x([+-]\d+)=0", eq_text)
# # # # # # #     if match:
# # # # # # #         a, b, c = 1, int(match.group(1)), int(match.group(2))
# # # # # # #         discriminant = b**2 - 4*a*c
# # # # # # #         x1 = (-b + discriminant**0.5) / (2*a)
# # # # # # #         x2 = (-b - discriminant**0.5) / (2*a)
# # # # # # #         steps = (
# # # # # # #             f"Equation: {a}x² + ({b})x + ({c}) = 0  \n"
# # # # # # #             f"Discriminant: Δ = b² - 4ac = {discriminant}  \n"
# # # # # # #             f"x1 = (-b + √Δ) / 2a = {x1}  \n"
# # # # # # #             f"x2 = (-b - √Δ) / 2a = {x2}"
# # # # # # #         )
# # # # # # #         return {"solution": [x1, x2], "steps": steps}

# # # # # # #     # Linear equation: ax + b = 0
# # # # # # #     match = re.match(r"([+-]?\d*)x([+-]\d+)=0", eq_text)
# # # # # # #     if match:
# # # # # # #         a = int(match.group(1)) if match.group(1) else 1
# # # # # # #         b = int(match.group(2))
# # # # # # #         x = -b / a
# # # # # # #         steps = f"Equation: {a}x + ({b}) = 0  \nSolution: x = -b/a = {x}"
# # # # # # #         return {"solution": [x], "steps": steps}

# # # # # # #     return {"solution": None, "steps": "Unsupported problem type"}


# # # # # # # agents/solver_agent.py
# # # # # # import re
# # # # # # import math

# # # # # # def solve_problem(problem_text):
# # # # # #     """
# # # # # #     Solve simple linear and quadratic equations.
# # # # # #     Returns solution and step-by-step explanation.
# # # # # #     """
# # # # # #     # Remove spaces
# # # # # #     eq = problem_text.replace(" ", "")

# # # # # #     # Quadratic pattern ax^2 + bx + c = 0
# # # # # #     match = re.match(r"([-+]?\d*)x\^2([-+]\d*)x([-+]\d*)=0", eq)
# # # # # #     if match:
# # # # # #         a = float(match.group(1)) if match.group(1) not in ["", "+", "-"] else float(match.group(1)+"1" if match.group(1) else 1)
# # # # # #         b = float(match.group(2) if match.group(2) else 1)
# # # # # #         c = float(match.group(3) if match.group(3) else 0)
# # # # # #         discriminant = b**2 - 4*a*c

# # # # # #         if discriminant < 0:
# # # # # #             solution = "No real roots"
# # # # # #             steps = f"Equation: {a}x^2 + {b}x + {c} = 0\nDiscriminant = {discriminant} < 0 → No real roots."
# # # # # #         else:
# # # # # #             x1 = (-b + math.sqrt(discriminant)) / (2*a)
# # # # # #             x2 = (-b - math.sqrt(discriminant)) / (2*a)
# # # # # #             solution = f"x1 = {x1}\nx2 = {x2}"
# # # # # #             steps = (
# # # # # #                 f"Equation: {a}x^2 + {b}x + {c} = 0\n"
# # # # # #                 f"Discriminant: D = b^2 - 4ac = {discriminant}\n"
# # # # # #                 f"x1 = (-b + √D)/(2a) = {x1}\n"
# # # # # #                 f"x2 = (-b - √D)/(2a) = {x2}"
# # # # # #             )
# # # # # #         return solution, steps

# # # # # #     # Linear pattern ax + b = 0
# # # # # #     match = re.match(r"([-+]?\d*)x([-+]\d*)=0", eq)
# # # # # #     if match:
# # # # # #         a = float(match.group(1)) if match.group(1) not in ["", "+", "-"] else float(match.group(1)+"1" if match.group(1) else 1)
# # # # # #         b = float(match.group(2))
# # # # # #         x = -b/a
# # # # # #         solution = f"x = {x}"
# # # # # #         steps = f"Equation: {a}x + {b} = 0 → x = -b/a = {x}"
# # # # # #         return solution, steps

# # # # # #     return "Unsupported problem", "Currently only linear and quadratic equations are supported."


# # # # # import re
# # # # # import sympy as sp

# # # # # def solve_problem(problem_text):
# # # # #     """
# # # # #     Solve linear or quadratic equations and return steps
# # # # #     """
# # # # #     steps = []
# # # # #     problem_text = problem_text.replace(" ", "").replace("\n", "")
    
# # # # #     # Identify quadratic: x^2 present
# # # # #     if "x^2" in problem_text:
# # # # #         try:
# # # # #             # Parse equation
# # # # #             x = sp.symbols('x')
# # # # #             eq = sp.sympify(problem_text.replace("=", "-(") + ")")
# # # # #             solution = sp.solve(eq, x)

# # # # #             steps.append(f"Equation to solve: {problem_text}")
# # # # #             steps.append(f"Using SymPy solve: {solution}")

# # # # #             solution_str = [f"x{i+1} = {sol.evalf()}" for i, sol in enumerate(solution)]
# # # # #             return solution_str, steps
# # # # #         except Exception as e:
# # # # #             return ["Unsupported problem"], ["Currently only linear and quadratic equations are supported."]
    
# # # # #     # Linear equation fallback
# # # # #     elif re.search(r'\d*x[+\-]?\d*=0', problem_text):
# # # # #         try:
# # # # #             x = sp.symbols('x')
# # # # #             eq = sp.sympify(problem_text.replace("=", "-(") + ")")
# # # # #             solution = sp.solve(eq, x)
# # # # #             steps.append(f"Equation to solve: {problem_text}")
# # # # #             steps.append(f"Using SymPy solve: {solution}")

# # # # #             solution_str = [f"x = {solution[0].evalf()}"]
# # # # #             return solution_str, steps
# # # # #         except:
# # # # #             return ["Unsupported problem"], ["Currently only linear and quadratic equations are supported."]

# # # # #     else:
# # # # #         return ["Unsupported problem"], ["Currently only linear and quadratic equations are supported."]

# # # # import re
# # # # import sympy as sp

# # # # def solve_problem(problem_text):
# # # #     """
# # # #     Solve linear or quadratic equations and return steps
# # # #     """
# # # #     steps = []

# # # #     # Remove extra words like "solve"
# # # #     problem_text = problem_text.lower().replace("solve", "")
# # # #     problem_text = problem_text.replace(" ", "").replace("\n", "")

# # # #     x = sp.symbols('x')

# # # #     # Quadratic: x^2 present
# # # #     if "x^2" in problem_text:
# # # #         try:
# # # #             # Convert '=' to '-(' for sympy
# # # #             eq = sp.sympify(problem_text.replace("=", "-(") + ")")
# # # #             solution = sp.solve(eq, x)
# # # #             steps.append(f"Equation to solve: {problem_text}")
# # # #             steps.append(f"Using SymPy solve: {solution}")

# # # #             solution_str = [f"x{i+1} = {sol.evalf()}" for i, sol in enumerate(solution)]
# # # #             return solution_str, steps
# # # #         except:
# # # #             return ["Unsupported problem"], ["Currently only linear and quadratic equations are supported."]

# # # #     # Linear equation fallback
# # # #     elif re.search(r'\d*x[+\-]?\d*=0', problem_text):
# # # #         try:
# # # #             eq = sp.sympify(problem_text.replace("=", "-(") + ")")
# # # #             solution = sp.solve(eq, x)
# # # #             steps.append(f"Equation to solve: {problem_text}")
# # # #             steps.append(f"Using SymPy solve: {solution}")

# # # #             solution_str = [f"x = {solution[0].evalf()}"]
# # # #             return solution_str, steps
# # # #         except:
# # # #             return ["Unsupported problem"], ["Currently only linear and quadratic equations are supported."]

# # # #     else:
# # # #         return ["Unsupported problem"], ["Currently only linear and quadratic equations are supported."]


# # # import sympy as sp

# # # def solve_problem(parsed):
# # #     """
# # #     Solve linear or quadratic equations and return step-by-step explanation.
# # #     """
# # #     problem_text = parsed["problem_text"]
# # #     x = sp.symbols('x')

# # #     try:
# # #         # Convert equation string into sympy expression
# # #         if "=" in problem_text:
# # #             lhs, rhs = problem_text.split("=")
# # #             eq = sp.sympify(f"({lhs}) - ({rhs})")
# # #         else:
# # #             eq = sp.sympify(problem_text)

# # #         # Solve the equation
# # #         solution = sp.solve(eq, x)
# # #         steps = [
# # #             f"Equation to solve: {problem_text}",
# # #             f"Using SymPy solve: {solution}"
# # #         ]
# # #         solution_str = [f"x{i+1} = {sol.evalf()}" for i, sol in enumerate(solution)]
# # #         return solution_str, steps
# # #     except:
# # #         return ["Unsupported problem"], ["Currently only linear and quadratic equations are supported."]


# # import re
# # import sympy as sp

# # # -----------------------------
# # # Utility to normalize equations
# # # -----------------------------
# # def normalize_equation(equation_text):
# #     """
# #     Clean the input string and convert it to standard sympy equation.
# #     Supports linear and quadratic equations like:
# #     x + 2 = 0
# #     x^2 - 5*x + 6 = 0
# #     """
# #     equation_text = equation_text.replace("^", "**")
# #     equation_text = equation_text.replace("=", "-(") + ")"  # Convert to 0 = ...
# #     return equation_text

# # # -----------------------------
# # # Solve linear equations
# # # -----------------------------
# # def solve_linear(equation):
# #     x = sp.symbols('x')
# #     eq = sp.sympify(equation)
# #     solution = sp.solve(eq, x)
# #     steps = [
# #         f"Original equation: {equation}",
# #         f"Isolate x and solve: {solution}"
# #     ]
# #     return solution, steps

# # # -----------------------------
# # # Solve quadratic equations
# # # -----------------------------
# # def solve_quadratic(equation):
# #     x = sp.symbols('x')
# #     eq = sp.sympify(equation)
# #     solution = sp.solve(eq, x)
# #     steps = [
# #         f"Original equation: {equation}",
# #         f"Factorize or apply quadratic formula: {solution}"
# #     ]
# #     return solution, steps

# # # -----------------------------
# # # Main solver function
# # # -----------------------------
# # def solve_problem(parsed_problem):
# #     """
# #     parsed_problem: dict with key "problem_text"
# #     Returns: solution list and step-by-step explanation
# #     """
# #     try:
# #         problem_text = parsed_problem["problem_text"]
# #         equation = normalize_equation(problem_text)

# #         # Determine if linear or quadratic
# #         if re.search(r"x\*\*2", equation):
# #             solution, steps = solve_quadratic(equation)
# #         elif re.search(r"x", equation):
# #             solution, steps = solve_linear(equation)
# #         else:
# #             return ["Unsupported problem"], ["Currently only linear and quadratic equations are supported."]

# #         # Format solution for Streamlit display
# #         solution_formatted = [f"x{i+1} = {val}" for i, val in enumerate(solution)]
# #         return solution_formatted, steps

# #     except Exception as e:
# #         return [f"Error: {str(e)}"], ["Failed to solve the problem."]



# import re
# import math


# # =========================
# # LINEAR EQUATION SOLVER
# # ax + b = c
# # =========================
# def solve_linear_equation(equation: str):
#     equation = equation.replace(" ", "")

#     match = re.match(r"([+-]?\d*)x([+-]\d+)?=([+-]?\d+)", equation)
#     if not match:
#         return None

#     a, b, c = match.groups()

#     a = int(a) if a not in ["", "+"] else 1
#     if a == "-":
#         a = -1

#     b = int(b) if b else 0
#     c = int(c)

#     steps = []
#     steps.append(f"Given equation: {a}x + {b} = {c}")
#     steps.append(f"Subtract {b} from both sides:")
#     steps.append(f"{a}x = {c - b}")
#     steps.append(f"Divide both sides by {a}:")
#     x = (c - b) / a
#     steps.append(f"x = {x}")

#     return "\n".join(steps)


# # =========================
# # QUADRATIC EQUATION SOLVER
# # ax² + bx + c = 0
# # =========================
# def solve_quadratic_equation(equation: str):
#     equation = equation.replace(" ", "")

#     match = re.match(
#         r"([+-]?\d*)x\^2([+-]\d+)x([+-]\d+)=0",
#         equation
#     )

#     if not match:
#         return None

#     a, b, c = match.groups()

#     a = int(a) if a not in ["", "+"] else 1
#     if a == "-":
#         a = -1

#     b = int(b)
#     c = int(c)

#     steps = []
#     steps.append(f"Given equation: {a}x² + {b}x + {c} = 0")
#     steps.append("Using quadratic formula:")
#     steps.append("x = (-b ± √(b² - 4ac)) / (2a)")

#     discriminant = b**2 - 4*a*c
#     steps.append(f"Discriminant = {b}² - 4×{a}×{c} = {discriminant}")

#     if discriminant < 0:
#         steps.append("Discriminant is negative → No real solutions")
#         return "\n".join(steps)

#     sqrt_d = math.sqrt(discriminant)
#     x1 = (-b + sqrt_d) / (2*a)
#     x2 = (-b - sqrt_d) / (2*a)

#     steps.append(f"x₁ = {x1}")
#     steps.append(f"x₂ = {x2}")

#     return "\n".join(steps)


# # =========================
# # MAIN SOLVER ENTRY
# # =========================
# def solve_problem(equation: str) -> str:
#     """
#     Try quadratic first, then linear
#     """
#     quad = solve_quadratic_equation(equation)
#     if quad:
#         return quad

#     lin = solve_linear_equation(equation)
#     if lin:
#         return lin

#     return "⚠️ Only linear and quadratic equations are supported in this version."



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
# def solve_quadratic_equation(equation: str):
#     equation = equation.replace(" ", "")

#     match = re.match(r"([+-]?\d*)x\^2([+-]\d+)x([+-]?\d+)=0", equation)
#     if not match:
#         return None

#     a, b, c = match.groups()
#     a = int(a) if a not in ["", "+"] else 1
#     if a == "-":
#         a = -1
#     b = int(b)
#     c = int(c)

#     steps = []
#     steps.append(f"Given equation: {a}x² + {b}x + {c} = 0")
#     steps.append("Using quadratic formula:")
#     steps.append("x = (-b ± √(b² - 4ac)) / (2a)")

#     discriminant = b**2 - 4*a*c
#     steps.append(f"Discriminant = {b}² - 4×{a}×{c} = {discriminant}")

#     # Handle complex roots
#     if discriminant < 0:
#         real_part = -b / (2*a)
#         imag_part = math.sqrt(abs(discriminant)) / (2*a)
#         steps.append("Discriminant is negative → complex roots")
#         steps.append(f"x₁ = {real_part} + {imag_part}i")
#         steps.append(f"x₂ = {real_part} - {imag_part}i")
#         return "\n".join(steps)

#     sqrt_d = math.sqrt(discriminant)
#     x1 = (-b + sqrt_d) / (2*a)
#     x2 = (-b - sqrt_d) / (2*a)
#     steps.append(f"x₁ = {x1}")
#     steps.append(f"x₂ = {x2}")

#     return "\n".join(steps)

def solve_quadratic_equation(equation: str):
    equation = equation.replace(" ", "")
    
    # Regex to handle implicit 1 coefficient: 1x^2-1x+6=0, 2x^2+3x+4=0
    match = re.match(r"([+-]?\d+)x\^2([+-]?\d+)x([+-]?\d+)=0", equation)
    if not match:
        return None

    a, b, c = match.groups()
    a, b, c = int(a), int(b), int(c)

    steps = []
    steps.append(f"Given equation: {a}x² + {b}x + {c} = 0")
    steps.append("Using quadratic formula: x = (-b ± √(b² - 4ac)) / (2a)")

    discriminant = b**2 - 4*a*c
    steps.append(f"Discriminant = {b}² - 4×{a}×{c} = {discriminant}")

    if discriminant < 0:
        sqrt_d = complex(0, abs(discriminant)**0.5)
        x1 = (-b + sqrt_d) / (2*a)
        x2 = (-b - sqrt_d) / (2*a)
    else:
        sqrt_d = discriminant**0.5
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
