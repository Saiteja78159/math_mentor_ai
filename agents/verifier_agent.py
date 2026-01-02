

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
