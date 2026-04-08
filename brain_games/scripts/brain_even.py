from brain_games.cli import DESCRIPTION, game, validate_answer


def main():
    try:
        game(DESCRIPTION, validate_answer)
    except KeyboardInterrupt:
        print("\nExit the game...")


if __name__ == "__main__":
    main()