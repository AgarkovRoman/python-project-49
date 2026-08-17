from brain_games.engine import start_game
from brain_games.games.prime import DESCRIPTION, generate_round


def main():
    start_game(DESCRIPTION, generate_round)


if __name__ == '__main__':
    main()
