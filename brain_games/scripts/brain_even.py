from brain_games.even import DESCRIPTION, validate_answer
from brain_games.matches.even_odd import play


def main():
    try:
        play(DESCRIPTION, validate_answer)
    except KeyboardInterrupt:
        print("\nExit the even game...")


if __name__ == "__main__":
    main()