from brain_games.constants import GAMES_CONSTANTS
from brain_games.core import play
from brain_games.games.gcd import get_round_data


def main() -> None:
    try:
        play(GAMES_CONSTANTS["GCD"]["DESCRIPTION"], get_round_data)
    except KeyboardInterrupt:
        print("\nExit the gcd game...")


if __name__ == "__main__":
    main()
