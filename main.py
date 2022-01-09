from crazy_cars import crazy_cars
from game_interface import GameInterface

def get_game() -> GameInterface:
    return crazy_cars.CrazyCars()


def main():
    game = get_game()
    game.new_game()

    while True:
        quit_game = game.game_closed()
        if not quit_game:
            game_over = game.play_round()
            if game_over:
                if game.try_again():
                    game.new_game()
                else:
                    quit_game = True

        if quit_game:
            game.end_game()


if __name__ == "__main__":
    main()
