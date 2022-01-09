import pygame
from pygame.constants import *


class GameSurface():
    def __init__(self, assets, width, height):
        # define frames per second
        self.__FPS = 60
        self.__framesPerSec = pygame.time.Clock()

        # colors
        self.__RED = (150, 0, 0)
        self.__BLACK = (0, 0, 0)

        # screen size
        self.__SCREEN_WIDTH = width
        self.__SCREEN_HEIGHT = height

        # fonts and labels
        self.__font = pygame.font.SysFont("Verdana", 60)
        self.__font_medium = pygame.font.SysFont("Verdana", 40)
        self.__font_small = pygame.font.SysFont("Verdana", 20)

        # assets
        # text images created using https://text.imageonline.co/
        # Font Type: Lukiest Guy
        # Color: #f0ae20
        # Bold: No
        self.__background = pygame.image.load(assets + '/images/animated_street.png')
        self.__collision = pygame.image.load(assets + '/images/collision.png')
        self.__collision = pygame.transform.scale(self.__collision, (90, 90))
        self.__game_over = pygame.image.load(assets + '/images/game_over.png')
        self.__game_over = pygame.transform.scale(self.__game_over, (375, 100))
        self.__get_ready = pygame.image.load(assets + '/images/get_ready.png')
        self.__get_ready = pygame.transform.scale(self.__get_ready, (375, 100))
        self.__new_high_score = pygame.image.load(assets + '/images/new_high_score.png')
        self.__play_again = pygame.image.load(assets + '/images/play_again.png')

    def get_screen_height(self):
        return self.__SCREEN_HEIGHT

    def get_screen_width(self):
        return self.__SCREEN_WIDTH

    def new_game_surface(self):
        self.__surface = pygame.display.set_mode(
            (self.__SCREEN_WIDTH, self.__SCREEN_HEIGHT))
        pygame.display.set_caption("Crazy Cars")

    def render_backgroud(self):
        self.__surface.blit(self.__background, (0, 0))

    def render_collision(self, player):
        x = player.rect.centerx - (self.__collision.get_width() / 2)
        y = player.rect.top - (self.__collision.get_height() / 2)
        self.__surface.blit(self.__collision, (x, y))
        pygame.display.update()

    def render_game_over(self, all_sprites):
        x = self.__get_x_center(self.__game_over)
        y = self.__get_y_center(self.__game_over)

        self.render_backgroud()
        self.__surface.blit(self.__game_over, (x, y))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()

    def render_game_score(self, score):
        s = self.__font_small.render(str(score), True, self.__BLACK)
        self.__surface.blit(s, (10, 560))

    def render_get_ready(self, player):
        x = self.__get_x_center(self.__get_ready)
        y = self.__get_y_center(self.__get_ready)

        self.render_backgroud()
        self.render_sprites([player])
        self.__surface.blit(self.__get_ready, (x, y))
        pygame.display.update()

    def render_high_score(self, score):
        s = self.__font_small.render(str(score), True, self.__BLACK)
        self.__surface.blit(s, (10, 10))

    def render_new_high_score(self, score):
        x = self.__get_x_center(self.__new_high_score)
        self.__surface.blit(self.__new_high_score, (x, 10))

        s = self.__font_medium.render(str(score), True, self.__BLACK)
        x = self.__get_x_center(s)
        self.__surface.blit(s, (x, 50))        

    def render_play_again(self):
        x = self.__get_x_center(self.__play_again)
        self.__surface.blit(self.__play_again, (x, 560))
        pygame.display.update()

    def render_sprites(self, all_sprites):
        for entity in all_sprites:
            self.__surface.blit(entity.image, entity.rect)
            entity.update(self.__SCREEN_WIDTH, self.__SCREEN_HEIGHT)

    def update(self):
        pygame.display.update()
        self.__framesPerSec.tick(self.__FPS)

    def __get_x_center(self, sprite):
        return (self.__SCREEN_WIDTH / 2) - (sprite.get_width() / 2)

    def __get_y_center(self, sprite):
        return (self.__SCREEN_HEIGHT / 2) - (sprite.get_height() / 2)
