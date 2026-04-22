import random
import math
import prompt

DESCRIPTION = "Find the greatest common divisor of given numbers."
WELCOME_TEXT = 'Welcome to the Brain Games!'
GREETING_INTRO_TEXT = 'May I have your name? '
GREETING_TEXT = 'Hello'
CORRECT_TEXT = 'yes'
ERROR_TEXT = 'no'
QUESTION_TEXT = 'Question:'
ANSWER_INTRO_TEXT = 'Your answer:'
END_ERROR_TEXT = 'is wrong answer ;(. Correct answer was'
END_ERROR_MESSAGE = "Let's try again,"
END_CORRECT_TEXT = 'Correct!'
END_CORRECT_MESSAGE = 'Congratulations, '
ROUNDS = 3


def retrieve_gcd(first_number: int, second_number: int) -> int:
    return math.gcd(first_number, second_number)


def logic(user_result, first, second):
    opertion = retrieve_gcd(first, second)
    validate_condition = ERROR_TEXT
    if opertion == int(user_result):
        validate_condition = CORRECT_TEXT
    return opertion, validate_condition


def play(logic):
    print(WELCOME_TEXT)
    name = prompt.string(GREETING_INTRO_TEXT)
    print(f"{GREETING_TEXT}, {name}!")
    print(DESCRIPTION)

    correct_answers = 0

    while correct_answers < ROUNDS:
    
        first_number = random.randint(1,100)
        second_number = random.randint(1,100)
        print(QUESTION_TEXT, first_number, second_number)
        user_answer = prompt.string(ANSWER_INTRO_TEXT)
        result, condition = logic(user_answer, first_number, second_number)
        print('debug: ', result)
        print('condition: ', condition)
        

        if 'no' == condition:
            print(f"'{user_answer}' {END_ERROR_TEXT} '{result}'.")  # noqa: E501
            print(f"{END_ERROR_MESSAGE} {name}!")
            return

        print(END_CORRECT_TEXT)
        correct_answers += 1

    print(f"{END_CORRECT_MESSAGE} {name}!")