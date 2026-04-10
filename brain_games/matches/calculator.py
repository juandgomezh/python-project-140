import prompt

INTENTS = 3


def play(desc, validate_answer):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(desc)
    print()

    correct_answers = 0

    while correct_answers < INTENTS:
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