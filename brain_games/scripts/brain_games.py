from brain_games.cli import welcome_user


def main():
    try:
        welcome_user()
    except KeyboardInterrupt:
        print("\nExit the first game...")
    

if __name__ == "__main__":
    
    main()