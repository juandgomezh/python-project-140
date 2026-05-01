import secrets

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2

    return True


def get_round_data():
    number = secrets.randbelow(100) + 1
    correct = "yes" if is_prime(number) else "no"
    return number, correct