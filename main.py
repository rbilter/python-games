from crazy_cars.crazy_cars import CrazyCars
from game_interface import GameInterface

def get_game() -> GameInterface:
    return CrazyCars()


def main():
    game = get_game()
    game.new_game()

    while True:
        quit_game_event = game.game_event()
        if not quit_game_event:
            game_over = game.play_round()
            if game_over:
                if game.try_again():
                    game.new_game()
                else:
                    quit_game_event = True

        if quit_game_event:
            game.end_game()


if __name__ == "__main__":
    main()
