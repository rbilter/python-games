import pygame
from pygame.constants import *


class GameSurface():
    def __init__(self, width, height):
        # define frames per second
        self.__FPS = 60
        self.__framesPerSec = pygame.time.Clock()

        # colors
        self.__BLUE = (0, 0, 255)
        self.__RED = (255, 0, 0)
        self.__GREEN = (0, 255, 0)
        self.__BLACK = (0, 0, 0)
        self.__WHITE = (255, 255, 255)

        # screen size
        self.__SCREEN_WIDTH = width
        self.__SCREEN_HEIGHT = height

        # fonts and labels
        self.__font = pygame.font.SysFont("Verdana", 60)
        self.__font_small = pygame.font.SysFont("Verdana", 20)

        # assets
        self.__background = pygame.image.load(
            "assets/images/animated_street.png")
        self.__collision = pygame.image.load("assets/images/collision.png")
        self.__collision = pygame.transform.scale(self.__collision, (90, 90))

    def get_screen_height(self):
        return self.__SCREEN_HEIGHT

    def get_screen_width(self):
        return self.__SCREEN_WIDTH

    def new_game_surface(self):
        self.surface = pygame.display.set_mode((400, 600))
        pygame.display.set_caption("Crazy Cars")

    def render_backgroud(self):
        self.surface.blit(self.__background, (0, 0))

    def render_collision(self, player):
        x = player.rect.centerx - (self.__collision.get_width() / 2)
        y = player.rect.top - (self.__collision.get_height() / 2)
        self.surface.blit(self.__collision, (x, y))
        pygame.display.update()

    def render_game_over(self, all_sprites):
        s = self.__font.render("Game Over", True, self.__BLACK)
        x = self.__get_x_center(s)
        y = self.__get_y_center(s)

        self.surface.fill(self.__RED)
        self.surface.blit(s, (x, y))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()

    def render_game_score(self, score):
        s = self.__font_small.render(str(score), True, self.__BLACK)
        self.surface.blit(s, (10, 560))

    def render_get_ready(self):
        s = self.__font.render("Get Ready!", True, self.__BLACK)
        x = self.__get_x_center(s)
        y = self.__get_y_center(s)

        self.surface.fill(self.__BLUE)
        self.surface.blit(s, (x, y))
        pygame.display.update()

    def render_high_score(self, score):
        s = self.__font_small.render(str(score), True, self.__BLACK)
        self.surface.blit(s, (10, 10))

    def render_new_high_score(self, score):
        s = self.__font_small.render(
            str(score) + ' IS A NEW HIGH SCORE!', True, self.__BLACK)
        self.surface.blit(s, (self.__get_x_center(s), 10))

    def render_play_again(self):
        s = self.__font_small.render(
            "Play Again? Yes(y) or No(n)", True, self.__BLACK)
        x = self.__get_x_center(s)
        self.surface.blit(s, (x, 560))
        pygame.display.update()

    def render_sprites(self, all_sprites):
        for entity in all_sprites:
            self.surface.blit(entity.image, entity.rect)
            entity.update(self.__SCREEN_WIDTH, self.__SCREEN_HEIGHT)

    def update(self):
        pygame.display.update()
        self.__framesPerSec.tick(self.__FPS)

    def __get_x_center(self, sprite):
        return (self.__SCREEN_WIDTH / 2) - (sprite.get_width() / 2)

    def __get_y_center(self, sprite):
        return (self.__SCREEN_HEIGHT / 2) - (sprite.get_height() / 2)
