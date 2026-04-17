from brain_games.calculator_helpers import DESCRIPTION, create_operation
from brain_games.games.calc import play


def main():
    try:
        play(DESCRIPTION, create_operation)
    except KeyboardInterrupt:
        print("\nExit the calculator game...")


if __name__ == "__main__":
    main()