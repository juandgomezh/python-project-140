import secrets

DESCRIPTION = "What number is missing in the progression?"


def get_round_data():
    size = 10
    start = secrets.randbelow(20) + 1
    step = secrets.randbelow(9) + 2

    progression = [start + i * step for i in range(size)]

    index = secrets.randbelow(len(progression))
    correct = progression[index]

    progression[index] = ".."

    question = " ".join(map(str, progression))

    return question, str(correct)