from brain_games.games.even import play, DESCRIPTION, validate_answer


def main():
    try:
        play(DESCRIPTION, validate_answer)
    except KeyboardInterrupt:
        print("\nExit the even game...")


if __name__ == "__main__":
    main()