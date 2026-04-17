import prompt

INTENTS = 3

def play(desc, create_answer):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(desc)

    for _ in range(INTENTS):
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