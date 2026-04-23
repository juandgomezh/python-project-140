import secrets

import prompt

DESCRIPTION = 'What is the result of the expression?'
OPERATIONS = ['+', '-', '*']
ROUNDS = 3


def create_operation():
    first_operand = secrets.randbelow(50) + 1
    second_operand = secrets.randbelow(50) + 1
    operator = secrets.choice(OPERATIONS) # nosec

    operation = f"{first_operand} {operator} {second_operand}"

    if operator == '+':
        result = first_operand + second_operand
    elif operator == '-':
        result = first_operand - second_operand
    else:
        result = first_operand * second_operand

    return operation, str(result)


def test():
    return 'test'


def play(desc, create_answer):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(desc)

    for _ in range(ROUNDS):
        question, correct = create_answer()

        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if correct == answer:
            print("Correct!")
        else:
            message = (
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct}'."
            )
            print(message)
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")