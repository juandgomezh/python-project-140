from brain_games.games.progression import play


def main():
    try:
        play()
    except KeyboardInterrupt:
        print("\nExit the progression game...")


if __name__ == "__main__":
    main()