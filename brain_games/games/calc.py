import secrets

DESCRIPTION = "What is the result of the expression?"
OPERATIONS = ["+", "-", "*"]


def get_round_data():
    first = secrets.randbelow(50) + 1
    second = secrets.randbelow(50) + 1
    operator = secrets.choice(OPERATIONS)

    question = f"{first} {operator} {second}"

    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    else:
        result = first * second

    return question, str(result)