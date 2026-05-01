import secrets

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_round_data():
    number = secrets.randbelow(100) + 1
    correct = "yes" if number % 2 == 0 else "no"
    return number, correct