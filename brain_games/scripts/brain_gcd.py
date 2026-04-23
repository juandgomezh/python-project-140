from brain_games.games.gcd import logic, play


def main():
    try:
        play(logic)
    except KeyboardInterrupt:
        print("\nExit the gcd game...")


if __name__ == "__main__":
    main()