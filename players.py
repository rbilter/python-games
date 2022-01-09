import pygame
from pygame.locals import *
import random


class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        super().__init__()
        self.image = pygame.image.load("assets/Player.png")
        self.rect = self.image.get_rect()
        self.screen_width = screen_width
        self.rect.center = (self.screen_width / 2, 520)

    def update(self, screen_height):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 35:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < self.screen_width - 35:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed, screen_width):
        super().__init__()
        self.image = pygame.image.load("assets/Enemy.png")
        self.rect = self.image.get_rect()
        self.screen_width = screen_width
        self.speed = speed
        self.score = 0
        self.reset_center()

    def increment_speed(self):
        self.speed += 0.5

    def get_score(self):
        return self.score

    def update(self, screen_height):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > screen_height:
            self.score += 1
            self.rect.top = 0
            self.reset_center()
    
    def reset_center(self):
        self.rect.center =  (random.randint(40, self.screen_width - 40), 0)
            
