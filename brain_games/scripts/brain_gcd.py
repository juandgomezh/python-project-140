from brain_games.games.gcd import play, logic


def main():
    try:
        play(logic)
    except KeyboardInterrupt:
        print("\nExit the gcd game...")


if __name__ == "__main__":
    main()