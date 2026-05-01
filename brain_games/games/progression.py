import secrets

DESCRIPTION = "What number is missing in the progression?"
WELCOME_TEXT = 'Welcome to the Brain Games!'
GREETING_INTRO_TEXT = 'May I have your name? '
GREETING_TEXT = 'Hello'
CORRECT_TEXT = 'yes'
ERROR_TEXT = 'no'
QUESTION_TEXT = 'Question:'
ANSWER_INTRO_TEXT = 'Your answer:'
END_ERROR_TEXT = 'is wrong answer ;(. Correct answer was'
END_ERROR_MESSAGE = "Let's try again,"
END_CORRECT_TEXT = '¡Correct!'
END_CORRECT_MESSAGE = 'Congratulations, '
ROUNDS = 3


def generate_progression(size=10):
    init = secrets.randbelow(20) + 1
    step = secrets.randbelow(9) + 2

    progresion = [init + i * step for i in range(size)]
    return progresion


def hide_number(progression):
    idx = secrets.randbelow(len(progression))
    correct = progression[idx]

    open_progression = progression.copy()
    open_progression[idx] = ".."

    return open_progression, correct


def format_answer(progression):
    return " ".join(map(str, progression))


def play():
    print(WELCOME_TEXT)

    name = input(GREETING_INTRO_TEXT)
    print(f"{GREETING_TEXT}, {name}!")

    for _ in range(ROUNDS):
        progression = generate_progression()
        open_progression, correct_answer = hide_number(progression)

        print(DESCRIPTION)
        print(f"{QUESTION_TEXT} {format_answer(open_progression)}")

        user_answer = input(ANSWER_INTRO_TEXT)

        if user_answer == str(correct_answer):
            print(END_CORRECT_TEXT)
        else:
            print(f"'{user_answer}' {END_ERROR_TEXT} '{correct_answer}'.")  # noqa: E501
            print(f"{END_ERROR_MESSAGE} {name}!")
            return

    print(f"{END_CORRECT_MESSAGE} {name}!")


if __name__ == "__main__":
    play()