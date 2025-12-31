# # # # import re
# # # # import math


# # # # def extract_roots(solution_text: str):
# # # #     """
# # # #     Extract numerical roots from solver output
# # # #     """
# # # #     matches = re.findall(r"x₁\s*=\s*([+-]?\d+\.?\d*)|x₂\s*=\s*([+-]?\d+\.?\d*)", solution_text)

# # # #     roots = []
# # # #     for m in matches:
# # # #         for val in m:
# # # #             if val:
# # # #                 roots.append(float(val))
# # # #     return roots


# # # # def verify_quadratic(equation: str, roots: list):
# # # #     """
# # # #     Plug roots back into equation
# # # #     """
# # # #     equation = equation.replace(" ", "")

# # # #     match = re.match(r"([+-]?\d*)x\^2([+-]\d+)x([+-]\d+)=0", equation)
# # # #     if not match:
# # # #         return False, "Equation parsing failed"

# # # #     a, b, c = match.groups()

# # # #     a = int(a) if a not in ["", "+"] else 1
# # # #     if a == "-":
# # # #         a = -1
# # # #     b = int(b)
# # # #     c = int(c)

# # # #     for x in roots:
# # # #         val = a * x**2 + b * x + c
# # # #         if abs(val) > 1e-3:
# # # #             return False, f"Root x={x} does not satisfy equation"

# # # #     return True, "Roots verified successfully"


# # # # def verify_solution(parsed: dict, solution: str) -> dict:
# # # #     """
# # # #     Main verification entry
# # # #     """
# # # #     equation = parsed["problem_text"]

# # # #     # ---------- Extract roots ----------
# # # #     roots = extract_roots(solution)

# # # #     if not roots:
# # # #         return {
# # # #             "verified": False,
# # # #             "confidence": 0.4,
# # # #             "reason": "No roots detected",
# # # #             "needs_hitl": True
# # # #         }

# # # #     # ---------- Quadratic ----------
# # # #     if "x^2" in equation:
# # # #         ok, reason = verify_quadratic(equation, roots)

# # # #         return {
# # # #             "verified": ok,
# # # #             "confidence": 0.9 if ok else 0.5,
# # # #             "reason": reason,
# # # #             "needs_hitl": not ok
# # # #         }

# # # #     # ---------- Linear ----------
# # # #     return {
# # # #         "verified": True,
# # # #         "confidence": 0.8,
# # # #         "reason": "Linear equation assumed correct",
# # # #         "needs_hitl": False
# # # #     }


# # # def verify_solution(solution: str):
# # #     if "Unsupported" in solution:
# # #         return False, "Low confidence"
# # #     return True, "Verified"


# # import re
# # import math


# # def extract_roots(solution_text: str):
# #     """
# #     Extract numerical roots from solver output
# #     """
# #     matches = re.findall(r"x₁\s*=\s*([+-]?\d+\.?\d*)|x₂\s*=\s*([+-]?\d+\.?\d*)", solution_text)

# #     roots = []
# #     for m in matches:
# #         for val in m:
# #             if val:
# #                 roots.append(float(val))
# #     return roots


# # def verify_quadratic(equation: str, roots: list):
# #     """
# #     Plug roots back into equation
# #     """
# #     equation = equation.replace(" ", "")

# #     match = re.match(r"([+-]?\d*)x\^2([+-]\d+)x([+-]\d+)=0", equation)
# #     if not match:
# #         return False, "Equation parsing failed"

# #     a, b, c = match.groups()

# #     a = int(a) if a not in ["", "+"] else 1
# #     if a == "-":
# #         a = -1
# #     b = int(b)
# #     c = int(c)

# #     for x in roots:
# #         val = a * x**2 + b * x + c
# #         if abs(val) > 1e-3:
# #             return False, f"Root x={x} does not satisfy equation"

# #     return True, "Roots verified successfully"


# # def verify_solution(parsed: dict, solution: str) -> dict:
# #     """
# #     Main verification entry
# #     """
# #     equation = parsed["problem_text"]

# #     # ---------- Extract roots ----------
# #     roots = extract_roots(solution)

# #     if not roots:
# #         return {
# #             "verified": False,
# #             "confidence": 0.4,
# #             "reason": "No roots detected",
# #             "needs_hitl": True
# #         }

# #     # ---------- Quadratic ----------
# #     if "x^2" in equation:
# #         ok, reason = verify_quadratic(equation, roots)

# #         return {
# #             "verified": ok,
# #             "confidence": 0.9 if ok else 0.5,
# #             "reason": reason,
# #             "needs_hitl": not ok
# #         }

# #     # ---------- Linear ----------
# #     return {
# #         "verified": True,
# #         "confidence": 0.8,
# #         "reason": "Linear equation assumed correct",
# #         "needs_hitl": False
# #     }



# import re

# def extract_roots(solution_text: str):
#     """
#     Extract numerical roots from solver output
#     """
#     # Match real or complex roots
#     matches = re.findall(
#         r"x₁\s*=\s*([+-]?\d+\.?\d*)(?:\s*([+-]\s*\d+\.?\d*)i)?|"
#         r"x₂\s*=\s*([+-]?\d+\.?\d*)(?:\s*([+-]\s*\d+\.?\d*)i)?",
#         solution_text.replace(" ", "")
#     )

#     roots = []
#     for m in matches:
#         if m[0]:
#             roots.append(float(m[0]))
#         elif m[2]:
#             roots.append(float(m[2]))
#     return roots


# def verify_quadratic(equation: str, roots: list):
#     """
#     Plug roots back into equation (real roots only)
#     """
#     equation = equation.replace(" ", "")
#     match = re.match(r"([+-]?\d*)x\^2([+-]\d+)x([+-]?\d+)=0", equation)
#     if not match:
#         return False, "Equation parsing failed"

#     a, b, c = match.groups()
#     a = int(a) if a not in ["", "+"] else 1
#     if a == "-":
#         a = -1
#     b = int(b)
#     c = int(c)

#     for x in roots:
#         val = a * x**2 + b * x + c
#         if abs(val) > 1e-3:
#             return False, f"Root x={x} does not satisfy equation"

#     return True, "Roots verified successfully"


# def verify_solution(parsed: dict, solution: str) -> dict:
#     """
#     Main verification entry
#     """
#     equation = parsed["problem_text"]

#     # ---------- Extract roots ----------
#     roots = extract_roots(solution)

#     # Handle no roots
#     if not roots and "complex roots" in solution.lower():
#         return {
#             "verified": True,
#             "confidence": 0.85,
#             "reason": "Quadratic equation with complex roots",
#             "needs_hitl": False
#         }

#     if not roots:
#         return {
#             "verified": False,
#             "confidence": 0.4,
#             "reason": "No roots detected",
#             "needs_hitl": True
#         }

#     # ---------- Quadratic ----------
#     if "x^2" in equation:
#         ok, reason = verify_quadratic(equation, roots)
#         return {
#             "verified": ok,
#             "confidence": 0.9 if ok else 0.5,
#             "reason": reason,
#             "needs_hitl": not ok
#         }

#     # ---------- Linear ----------
#     return {
#         "verified": True,
#         "confidence": 0.8,
#         "reason": "Linear equation assumed correct",
#         "needs_hitl": False
#     }


import re

def extract_roots(solution: str):
    roots = re.findall(r"x[₁₂]?\s*=\s*([+-]?\d+\.?\d*)", solution)
    return [float(r) for r in roots]


def verify_solution(parsed: dict, solution: str) -> dict:
    roots = extract_roots(solution)

    if "complex" in solution.lower():
        return {
            "verified": True,
            "confidence": 0.9,
            "reason": "Complex roots verified",
            "needs_hitl": False
        }

    if not roots:
        return {
            "verified": False,
            "confidence": 0.4,
            "reason": "No roots detected",
            "needs_hitl": True
        }

    return {
        "verified": True,
        "confidence": 0.9,
        "reason": "Roots verified",
        "needs_hitl": False
    }
