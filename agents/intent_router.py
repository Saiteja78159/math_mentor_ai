# # # def route_intent(parsed: dict) -> str:
# # #     topic = parsed.get("topic", "unknown")

# # #     if topic == "algebra":
# # #         return "ALGEBRA_SOLVER"
# # #     if topic == "calculus":
# # #         return "CALCULUS_SOLVER"
# # #     if topic == "probability":
# # #         return "PROBABILITY_SOLVER"

# # #     return "GENERAL_SOLVER"


# # def route_intent(parsed: dict) -> str:
# #     topic = parsed.get("topic", "unknown")

# #     if topic == "algebra":
# #         return "ALGEBRA_SOLVER"
# #     if topic == "calculus":
# #         return "CALCULUS_SOLVER"
# #     if topic == "probability":
# #         return "PROBABILITY_SOLVER"

# #     return "GENERAL_SOLVER"


# # agents/intent_router.py
# def route_intent(problem: str) -> str:
#     if "x**2" in problem:
#         return "quadratic"
#     if "x" in problem and "=" in problem:
#         return "linear"
#     return "unsupported"


def route_intent(parsed: dict) -> str:
    topic = parsed.get("topic", "unknown")

    if topic == "algebra":
        return "ALGEBRA_SOLVER"
    if topic == "calculus":
        return "CALCULUS_SOLVER"
    if topic == "probability":
        return "PROBABILITY_SOLVER"

    return "GENERAL_SOLVER"
