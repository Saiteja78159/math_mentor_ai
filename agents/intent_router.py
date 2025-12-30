def route_intent(parsed: dict) -> str:
    topic = parsed.get("topic", "unknown")

    if topic == "algebra":
        return "ALGEBRA_SOLVER"
    if topic == "calculus":
        return "CALCULUS_SOLVER"
    if topic == "probability":
        return "PROBABILITY_SOLVER"

    return "GENERAL_SOLVER"
