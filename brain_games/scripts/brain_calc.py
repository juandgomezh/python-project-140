from brain_games.games.calc import play, DESCRIPTION, create_operation


def main():
    try:
        play(DESCRIPTION, create_operation)
    except KeyboardInterrupt:
        print("\nExit the calculator game...")


if __name__ == "__main__":
    main()