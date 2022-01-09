from os import truncate
from crazy_cars import CrazyCars


def main():
    cc = CrazyCars()
    cc.new_game()
    while True:
        quit_game = cc.game_closed()
        if not quit_game:
            game_over = cc.play_round()
            if game_over:
                if cc.try_again():
                    cc.new_game()
                else:
                    quit_game = True

        if quit_game:
            cc.end_game()


if __name__ == "__main__":
    main()
