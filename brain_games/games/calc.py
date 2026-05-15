import random

from brain_games.constants import GAMES_CONSTANTS


def get_round_data() -> tuple[str, str]:
    # se extraen las constantes y se usa la funcion de math.random
    first = random.randint(
        GAMES_CONSTANTS["ALL"]["MIN_NUMBER"],
        GAMES_CONSTANTS["CALC"]["MAX_NUMBER"],
    )  # nosec B311
    second = random.randint(
        GAMES_CONSTANTS["ALL"]["MIN_NUMBER"],
        GAMES_CONSTANTS["CALC"]["MAX_NUMBER"],
    )  # nosec B311
    operator = operator = random.choice(GAMES_CONSTANTS["CALC"]["OPERATIONS"])  # nosec B311

    question = f"{first} {operator} {second}"

    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    else:
        result = first * second

    return question, str(result)
