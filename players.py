import pygame
from pygame.locals import *
import random


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/player.png")
        self.rect = self.image.get_rect()

    def get_center(self):
        return self.rect.center

    def reset_center(self, screen_width):
        self.rect.center = (screen_width / 2, 520)

    def update(self, screen_width, screen_height):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 35:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < screen_width - 35:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.image.load("assets/images/enemy.png")
        self.rect = self.image.get_rect()
        self.__speed = speed
        self.__laps = 0

    def get_laps(self):
        return self.__laps

    def increment_speed(self):
        self.__speed += 0.5

    def reset_center(self, screen_width):
        self.rect.center = (random.randint(40, screen_width - 40), 0)

    def update(self, screen_width, screen_height):
        self.rect.move_ip(0, self.__speed)
        if self.rect.bottom > screen_height:
            self.rect.top = 0
            self.reset_center(screen_width)
            self.__laps += 1
