# imports
from crazy_cars import players
from crazy_cars import settings
from crazy_cars import sound
from crazy_cars import surface
from game_interface import GameInterface
import pygame
from pygame.constants import *
import sys
import time


class CrazyCars(GameInterface):
    def __init__(self):
        pygame.init()

        # assets sub folder
        self.__assets = "crazy_cars/assets"

        # game surface width and height
        self.__SURFACE_WIDTH = 400
        self.__SURFACE_HEIGHT = 600

        # game surface
        self.__game_surface = surface.GameSurface(self.__assets,
            self.__SURFACE_WIDTH, 
            self.__SURFACE_HEIGHT)
        self.__game_surface.new_game_surface()

        # game settings
        self.__game_settings = settings.GameSettings(self.__assets)
        self.__game_speed = 5

        # game sound
        self.__game_sound = sound.Sound(self.__assets)

        # user event
        self.__INC_SPEED = pygame.USEREVENT + 1
        pygame.time.set_timer(self.__INC_SPEED, 1000)

    def end_game(self):
        pygame.quit()
        sys.exit()

    def game_closed(self) -> bool:
        close = False
        for event in pygame.event.get():
            if event.type == self.__INC_SPEED:
                self.__E1.increment_speed()
                break
            if event.type == QUIT:
                close = True
                break
        return close

    def new_game(self):
        self.__P1 = players.Player(self.__assets)
        self.__P1.reset_center(self.__SURFACE_WIDTH)
        self.__E1 = players.Enemy(self.__assets, self.__game_speed)
        self.__E1.reset_center(self.__SURFACE_WIDTH)

        self.__enemies = pygame.sprite.Group()
        self.__enemies.add(self.__E1)
        self.__all_sprites = pygame.sprite.Group()
        self.__all_sprites.add(self.__P1)
        self.__all_sprites.add(self.__E1)
        self.__game_surface.render_get_ready()
        
        self.__sleep(2)
        self.__game_sound.play_backgroud_music()

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
        self.__game_sound.stop()
        self.__game_surface.render_collision(self.__P1)
        self.__game_sound.play_crash()
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