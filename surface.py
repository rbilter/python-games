import pygame
from pygame import surface
from pygame.constants import *


class GameSurface():
    def __init__(self, width, height):
        # define frames per second
        self.FPS = 60
        self.framesPerSec = pygame.time.Clock()

        # colors
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        # screen size
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height

        # fonts and labels
        self.font = pygame.font.SysFont("Verdana", 60)
        self.font_small = pygame.font.SysFont("Verdana", 20)
        self.GAME_OVER_LABEL = "Game Over"
        self.PLAY_AGAIN_LABEL = "Play Again? Yes(y) or No(n)"
        self.GET_READY_LABEL = "Get Ready!"
        self.NEW_HIGH_SCORE = "IS A NEW HIGH SCORE!"

        # assets
        self.background = pygame.image.load("assets/images/animated_street.png")
        self.collision = pygame.image.load("assets/images/collision.png")
        self.collision = pygame.transform.scale(self.collision, (90, 90))

    def get_screen_height(self):
        return self.SCREEN_HEIGHT

    def get_screen_width(self):
        return self.SCREEN_WIDTH

    def new_game_surface(self):
        self.surface = pygame.display.set_mode((400, 600))
        pygame.display.set_caption("Crazy Cars")

    def render_backgroud(self):
        self.surface.blit(self.background, (0, 0))

    def render_collision(self, player):
        x = player.rect.centerx - (self.collision.get_width() / 2)
        y = player.rect.top - (self.collision.get_height() / 2)
        self.surface.blit(self.collision, (x, y))
        pygame.display.update()

    def render_game_over(self, all_sprites):
        s = self.font.render(self.GAME_OVER_LABEL, True, self.BLACK)
        x = self.__get_x_center(s)
        y = self.__get__y_center(s)
        
        self.surface.fill(self.RED)
        self.surface.blit(s, (x, y))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()

    def render_game_score(self, score):
        s = self.font_small.render(str(score), True, self.BLACK)
        self.surface.blit(s, (10, 560))

    def render_get_ready(self):
        s = self.font.render(self.GET_READY_LABEL, True, self.BLACK)
        x = self.__get_x_center(s)
        y = self.__get__y_center(s)
       
        self.surface.fill(self.BLUE)
        self.surface.blit(s, (x, y))
        pygame.display.update()

    def render_high_score(self, score):
        s = self.font_small.render(str(score), True, self.BLACK)
        self.surface.blit(s, (10, 10))

    def render_new_high_score(self, score):
        s = self.font_small.render(str(score) + ' ' + self.NEW_HIGH_SCORE, True, self.BLACK)
        self.surface.blit(s, (self.__get_x_center(s), 10))

    def render_play_again(self):
        s = self.font_small.render(self.PLAY_AGAIN_LABEL, True, self.BLACK)
        x = self.__get_x_center(s)
        self.surface.blit(s, (x, 560))
        pygame.display.update()

    def render_sprites(self, all_sprites):
        for entity in all_sprites:
            self.surface.blit(entity.image, entity.rect)
            entity.update(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

    def update(self):
        pygame.display.update()
        self.framesPerSec.tick(self.FPS)

    def __get_x_center(self, sprite):
        return (self.SCREEN_WIDTH / 2) - (sprite.get_width() / 2)

    def __get__y_center(self, sprite):
        return (self.SCREEN_HEIGHT / 2) - (sprite.get_height() / 2)
