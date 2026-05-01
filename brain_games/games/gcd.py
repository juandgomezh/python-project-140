import math
import secrets

DESCRIPTION = "Find the greatest common divisor of given numbers."


def get_round_data():
    a = secrets.randbelow(100) + 1
    b = secrets.randbelow(100) + 1

    question = f"{a} {b}"
    correct = str(math.gcd(a, b))

    return question, correct