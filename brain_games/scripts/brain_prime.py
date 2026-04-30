from brain_games.games.prime import play


def main():
    try:
        play()
    except KeyboardInterrupt:
        print("\nExit the prime game...")


if __name__ == "__main__":
    main()