import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
WELCOME_TEXT = "Welcome to the Brain Games!"
GREETING_INTRO_TEXT = "May I have your name? "
GREETING_TEXT = "Hello"
CORRECT_TEXT = "Correct!"
ERROR_TEXT = "is wrong answer ;(. Correct answer was"
ERROR_MESSAGE = "Let's try again,"
END_CORRECT_MESSAGE = "Congratulations,"
QUESTION_TEXT = "Question:"
ANSWER_INTRO_TEXT = "Your answer:"
ROUNDS = 3


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


def generate_question():
    number = random.randint(1, 100)
    correct_answer = "yes" if is_prime(number) else "no"
    return number, correct_answer


def play():
    print(WELCOME_TEXT)

    name = input(GREETING_INTRO_TEXT)
    print(f"{GREETING_TEXT}, {name}!")

    print(DESCRIPTION)

    for _ in range(ROUNDS):
        number, correct_answer = generate_question()

        print(f"{QUESTION_TEXT} {number}")
        user_answer = input(ANSWER_INTRO_TEXT).strip().lower()

        if user_answer == correct_answer:
            print(CORRECT_TEXT)
        else:
            print(f"'{user_answer}' {ERROR_TEXT} '{correct_answer}'.")
            print(f"{ERROR_MESSAGE} {name}!")
            return

    print(f"{END_CORRECT_MESSAGE} {name}!")


if __name__ == "__main__":
    play()