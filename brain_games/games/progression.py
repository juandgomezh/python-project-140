import random

from brain_games.constants import GAMES_CONSTANTS


def get_round_data() -> tuple[str, str]:
    size = GAMES_CONSTANTS["PROGRESSION"]["PROGRESSION_SIZE"]
    start = random.randint(
        GAMES_CONSTANTS["ALL"]["MIN_NUMBER"],
        GAMES_CONSTANTS["PROGRESSION"]["MAX_NUMBER"],
    )  # nosec B311

    step = random.randint(
        GAMES_CONSTANTS["PROGRESSION"]["MIN_STEP_NUMBER"],
        GAMES_CONSTANTS["PROGRESSION"]["MAX_STEP_NUMBER"],
    )  # nosec B311

    progression_list = [start + i * step for i in range(size)]

    index = random.randint(
        GAMES_CONSTANTS["ALL"]["MIN_NUMBER"], len(progression_list) - 1
    )  # nosec B311
    correct = progression_list[index]

    progression_list[index] = ".."

    question = " ".join(map(str, progression_list))

    return question, str(correct)
