from brain_games.calculator_helpers import DESCRIPTION, validate_answer
from brain_games.matches.calc import play


def main():
    try:
        play(DESCRIPTION, validate_answer)
    except KeyboardInterrupt:
        print("\nExit the calculator game...")


if __name__ == "__main__":
    main()