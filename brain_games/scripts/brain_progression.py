from brain_games.constants import GAMES_CONSTANTS
from brain_games.core import play
from brain_games.games.progression import get_round_data


def main() -> None:
    try:
        play(GAMES_CONSTANTS["PROGRESSION"]["DESCRIPTION"], get_round_data)
    except KeyboardInterrupt:
        print("\nExit the progression game...")


if __name__ == "__main__":
    main()
