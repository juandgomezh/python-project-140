import random

from brain_games.constants import GAMES_CONSTANTS


def is_prime(number: int) -> bool:
    if number < 2:  # 1 y 2 no son primos
        return False
    if number == 2:  # 2 es primo
        return True

    position = 3  # comienza en tres, ya se evaluaron los anteriores

    while position < number:  # probamos todos los números menores que number
        if number % position == 0:
            return False  # si es divisible, no es primo

        position += 1

    return True


# devuelve una tupla donde esta el num aleatorio y
# si es correcta o no la afirmación
def get_round_data() -> tuple[str, str]:
    number = random.randint(
        GAMES_CONSTANTS["ALL"]["MIN_NUMBER"],
        GAMES_CONSTANTS["PRIME"]["MAX_NUMBER"],
    )  # nosec B311
    correct = "yes" if is_prime(number) else "no"
    return number, correct
