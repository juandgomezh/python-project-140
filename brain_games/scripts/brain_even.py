from brain_games.cli import DESCRIPTION, validate_answer, game


def main():
    try:
        game(DESCRIPTION, validate_answer)
    except KeyboardInterrupt:
        print("\nExit the game...")

if __name__ == "__main__":
    main()