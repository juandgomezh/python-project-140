import prompt
import random

DESCRIPTION = 'What is the result of the expression?'
OPERATIONS = ['+', '-', '*']
ROUNDS = 3

def create_operation():
    first_operand = random.randint(1, 50)
    second_operand = random.randint(1, 50)
    operator = random.choice(OPERATIONS)

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
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")