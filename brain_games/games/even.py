import random

from brain_games.constants import GAMES_CONSTANTS


def get_round_data() -> tuple[str, str]:
    number = random.randint(
        GAMES_CONSTANTS["ALL"]["MIN_NUMBER"],
        GAMES_CONSTANTS["EVEN"]["MAX_NUMBER"],
    )  # nosec B311
    correct = "yes" if number % 2 == 0 else "no"
    return number, correct
