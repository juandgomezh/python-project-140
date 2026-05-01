from brain_games.core import play
from brain_games.games.even import DESCRIPTION, get_round_data


def main():
    try:
        play(DESCRIPTION, get_round_data)
    except KeyboardInterrupt:
        print("\nExit the even game...")


if __name__ == "__main__":
    main()