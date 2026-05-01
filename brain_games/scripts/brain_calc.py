from brain_games.core import play
from brain_games.games.calc import DESCRIPTION, get_round_data

    
def main():
    try:
        play(DESCRIPTION, get_round_data)
    except KeyboardInterrupt:
        print("\nExit the calc game...")


if __name__ == "__main__":
    main()