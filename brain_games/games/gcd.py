import math
import random

from brain_games.constants import GAMES_CONSTANTS


def get_round_data() -> tuple[str, str]:
    a = random.randint(
        GAMES_CONSTANTS["ALL"]["MIN_NUMBER"],
        GAMES_CONSTANTS["GCD"]["MAX_NUMBER"],
    )  # nosec B311
    b = random.randint(
        GAMES_CONSTANTS["ALL"]["MIN_NUMBER"],
        GAMES_CONSTANTS["GCD"]["MAX_NUMBER"],
    )  # nosec B311

    question = f"{a} {b}"
    correct = str(math.gcd(a, b))

    return question, correct
