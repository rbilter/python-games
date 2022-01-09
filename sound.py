import pygame


class Sound():
    def __init__(self):
        # used to store the current sound being played
        self.__current_sound = None

    def play_backgroud_music(self):
        s = pygame.mixer.Sound('assets/sounds/action_rock.mp3')
        self.__current_sound = s.play()

    def play_crash(self):
        s = pygame.mixer.Sound('assets/sounds/crash.wav')
        s.play()

    def stop(self):
        if self.__current_sound != None:
            self.__current_sound.stop()
