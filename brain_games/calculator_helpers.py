import random

DESCRIPTION = 'What is the result of the expression?'
OPERATIONS = ['+', '-', '*']

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