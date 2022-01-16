import pygame

class GameInterface:
    def __init__(self):
        pygame.init()

    def end_game(self):
        """will be called by main to close the game so use for any clean up"""
        pass

    def game_event(self):
        """check the game even, return true if the QUIT event was executed"""
        pass

    def new_game(self):
        """initalize the game"""
        pass

    def play_round(self) -> bool:
        """play one round of the game return true, false to end the game"""
        pass

    def try_again(self) -> bool:
        """show try again option, true to continue playing false to end the game"""
        pass
