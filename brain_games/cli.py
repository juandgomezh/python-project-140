import random

import prompt

INTENTS = 3
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    

def is_even_condition(number):
    return number % 2 == 0


def validate_answer():
    number = random.randint(1, 100)
    correct = "yes" if is_even_condition(number) else "no"
    return number, correct


def game(desc, validate_answer):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(desc)

    correct_answers = 0

    while correct_answers < INTENTS:
        question, correct = validate_answer()

        print(f"Question: {question}")
        user = prompt.string("Your answer: ")

        if user != correct:
            print(f"'{user}' is wrong answer ;(.")
            print(f"Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")
        correct_answers += 1

    print(f"Congratulations, {name}!")