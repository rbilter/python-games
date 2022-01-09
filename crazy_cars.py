# imports
import players
import pygame
from pygame.constants import *
import settings
import surface
import sys
import time


class CrazyCars():
    def __init__(self):
        pygame.init()

        # game surface width and height
        self.SURFACE_WIDTH = 400
        self.SURFACE_HEIGHT = 600

        # game surface
        self.game_surface = surface.GameSurface(
            self.SURFACE_WIDTH, self.SURFACE_HEIGHT)
        self.game_surface.new_game_surface()

        # game settings
        self.gs = settings.GameSettings()
        self.high_score = self.gs.get_high_score()
        self.game_speed = 5

        # user event
        self.INC_SPEED = pygame.USEREVENT + 1
        pygame.time.set_timer(self.INC_SPEED, 1000)

    def end_game(self):
        pygame.quit()
        sys.exit()

    def game_closed(self):
        close = False
        for event in pygame.event.get():
            if event.type == self.INC_SPEED:
                self.E1.increment_speed()
            if event.type == QUIT:
                close = True
        return close

    def had_collision(self):
        return pygame.sprite.spritecollideany(self.P1, self.enemies)

    def new_game(self):
        self.P1 = players.Player()
        self.P1.reset_center(self.SURFACE_WIDTH)
        self.E1 = players.Enemy(self.game_speed)
        self.E1.reset_center(self.SURFACE_WIDTH)

        self.enemies = pygame.sprite.Group()
        self.enemies.add(self.E1)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.P1)
        self.all_sprites.add(self.E1)
        self.game_surface.render_get_ready()
        time.sleep(2)

    def play_round(self):
        game_over = False

        score = self.E1.get_laps()
        if self.high_score < score:
            self.high_score = score

        self.game_surface.render_backgroud()
        self.game_surface.render_game_score(score)
        self.game_surface.render_high_score(self.high_score)
        self.game_surface.render_sprites(self.all_sprites)

        if self.had_collision():
            self.game_surface.render_collision(self.P1)
            time.sleep(1.5)

            self.game_surface.render_game_over(self.all_sprites)
            self.gs.set_high_score(self.high_score)
            time.sleep(2.0)
            game_over = True
        else:
            self.game_surface.update()
        return game_over

    def try_again(self):
        try_again = False
        while True:
            key_pressed = False
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_n:
                    key_pressed = True
                if event.type == KEYDOWN and event.key == K_y:
                    try_again = True
                    key_pressed = True
                if event.type == QUIT:
                    try_again = False
                    key_pressed = True

            if not key_pressed:
                self.game_surface.render_play_again()
            else:
                break
        return try_again
