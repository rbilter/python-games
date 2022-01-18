# imports
from crazy_cars.players import Enemy, Player
from crazy_cars.settings import GameSettings
from crazy_cars.sound import Sound, Sounds
from crazy_cars.surface import GameSurface
from game_interface import GameInterface
import pygame
from pygame.constants import *
import sys
import time


class CrazyCars(GameInterface):
    def __init__(self):
        super().__init__()

        # assets sub folder
        self.__assets = "crazy_cars/assets"

        # game surface width and height
        self.__SURFACE_WIDTH = 400
        self.__SURFACE_HEIGHT = 600

        # game surface
        self.__game_surface = GameSurface(self.__assets,
            self.__SURFACE_WIDTH, 
            self.__SURFACE_HEIGHT)
        self.__game_surface.new_game_surface()

        # game settings
        self.__game_settings = GameSettings(self.__assets)
        self.__game_speed = 5

        # game sound
        self.__game_sound = Sound(self.__assets)

        # user event
        self.__INC_SPEED = pygame.USEREVENT + 1
        pygame.time.set_timer(self.__INC_SPEED, 1000)

    def game_event(self) -> bool:
        close = False
        for event in pygame.event.get():
            if event.type == KEYUP:
                self.__game_sound.stop(Sounds.TIRE_SCREECH)
            if event.type == KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[K_LEFT] or pressed_keys[K_RIGHT]:
                    self.__game_sound.play(Sounds.TIRE_SCREECH)
            if event.type == self.__INC_SPEED:
                self.__E1.increment_speed()
            if event.type == QUIT:
                close = True
        return close

    def new_game(self):
        self.__P1 = Player(self.__assets)
        self.__P1.reset_center(self.__SURFACE_WIDTH)
        self.__E1 = Enemy(self.__assets, self.__game_speed)
        self.__E1.reset_center(self.__SURFACE_WIDTH)

        self.__enemies = pygame.sprite.Group()
        self.__enemies.add(self.__E1)
        self.__all_sprites = pygame.sprite.Group()
        self.__all_sprites.add(self.__P1)
        self.__all_sprites.add(self.__E1)
        self.__game_surface.render_get_ready(self.__P1)
        
        self.__sleep(2)
        self.__game_sound.play(Sounds.BACKGROUND)

    def play_round(self) -> bool:
        game_over = False
        score = self.__play_round()
        if self.__had_collision():
            self.__play_collision()
            self.__play_game_over(score)
            game_over = True
        else:
            self.__game_surface.update()
        return game_over

    def try_again(self) -> bool:
        try_again = False
        while True:
            key_pressed = False
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_n:
                    key_pressed = True
                    break
                if event.type == KEYDOWN and event.key == K_y:
                    try_again = True
                    key_pressed = True
                    break
                if event.type == QUIT:
                    key_pressed = True
                    break

            if not key_pressed:
                self.__game_surface.render_play_again()
            else:
                break
        return try_again

    def __had_collision(self):
        return pygame.sprite.spritecollideany(self.__P1, self.__enemies)

    def __play_collision(self):
        self.__game_sound.stop(Sounds.BACKGROUND)
        self.__game_sound.stop(Sounds.TIRE_SCREECH)
        self.__game_sound.play(Sounds.CRASH)
        self.__game_surface.render_collision(self.__P1)
        self.__sleep(1.5)

    def __play_game_over(self, score):
        self.__game_surface.render_game_over(self.__all_sprites)
        if self.__game_settings.set_high_score(score):
            self.__game_surface.render_new_high_score(score)
        self.__sleep(2.0)

    def __play_round(self):
        score = self.__E1.get_laps()
        self.__game_surface.render_backgroud()
        self.__game_surface.render_game_score(score)
        self.__game_surface.render_high_score(
            self.__game_settings.get_high_score())
        self.__game_surface.render_sprites(self.__all_sprites)
        return score

    def __sleep(self, seconds):
        time.sleep(seconds)