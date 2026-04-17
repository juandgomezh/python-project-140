import prompt
import secrets

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
ROUNDS = 3

def is_even_condition(number):
    return number % 2 == 0

def validate_answer():
    number = secrets.randbelow(100) + 1
    correct = "yes" if is_even_condition(number) else "no"
    return number, correct

def play(desc, validate_answer):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(desc)
    print()

    correct_answers = 0

    while correct_answers < ROUNDS:
        question, correct = validate_answer()

        print(f"Question: {question}")
        user = prompt.string("Your answer: ")

        if user != correct:
            print(f"'{user}' is wrong answer ;(. Correct answer was '{correct}'.")  # noqa: E501
            print(f"Let's try again, {name}!")
            return

        print("Correct!")
        correct_answers += 1

    print(f"Congratulations, {name}!")