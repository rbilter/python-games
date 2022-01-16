from enum import Enum
import pygame

class Sounds(Enum):
    BACKGROUND = 1
    CRASH = 2
    TIRE_SCREECH = 3

class Sound():
    def __init__(self, assets):
        self.__backgroud = pygame.mixer.Sound(assets + '/sounds/action_rock.mp3')
        self.__crash = pygame.mixer.Sound(assets + '/sounds/crash.wav')         
        self.__tire_screech = pygame.mixer.Sound(assets + '/sounds/tire_screech.mp3')

    def play(self, sound):
        if sound == Sounds.BACKGROUND:
            self.__backgroud.play()
        elif sound == Sounds.CRASH:
            self.__crash.play()
        elif sound == Sounds.TIRE_SCREECH:
            self.__tire_screech.play()

    def stop(self, sound):
        if sound == Sounds.BACKGROUND:
            self.__backgroud.stop()
        elif sound == Sounds.CRASH:
            self.__crash.stop()
        elif sound == Sounds.TIRE_SCREECH:
            self.__tire_screech.stop()
