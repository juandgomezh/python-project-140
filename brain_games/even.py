import secrets

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even_condition(number):
    return number % 2 == 0


def validate_answer():
    number = secrets.randbelow(100) + 1
    correct = "yes" if is_even_condition(number) else "no"
    return number, correct
