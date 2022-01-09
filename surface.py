import players
import pygame
from pygame.constants import *


class GameSurface():
    def __init__(self):
        pygame.init()

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
        self.SCREEN_WIDTH = 400
        self.SCREEN_HEIGHT = 600

        # fonts and labels
        self.font = pygame.font.SysFont("Verdana", 60)
        self.font_small = pygame.font.SysFont("Verdana", 20)
        self.GAME_OVER_LABEL = self.font.render("Game Over", True, self.BLACK)
        self.PLAY_AGAIN_LABEL = self.font_small.render(
            "Play Again? Yes(y) or No(n)", True, self.BLACK)
        self.GET_READY_LABEL = self.font.render("Get Ready!", True, self.BLACK)

        # assets
        self.background = pygame.image.load("assets/AnimatedStreet.png")
        self.collision = pygame.image.load("assets/collision.png")
        self.collision = pygame.transform.scale(self.collision, (90, 90))

    def get_screen_width(self):
        return self.SCREEN_WIDTH

    def had_collision(self, player, enemies):
        return pygame.sprite.spritecollideany(player, enemies)

    def new_game_surface(self):
        self.surface = pygame.display.set_mode((400, 600))
        pygame.display.set_caption("Crazy Cars")

    def quit(self):
        pygame.quit()

    def render_backgroud(self):
        self.surface.blit(self.background, (0, 0))

    def render_collision(self, player):
        x = player.rect.centerx - (self.collision.get_width() / 2)
        y = player.rect.top - (self.collision.get_height() / 2)
        self.surface.blit(self.collision, (x, y))
        pygame.display.update()
        pygame.mixer.Sound('assets/crash.wav').play()

    def render_game_over(self, all_sprites):
        self.surface.fill(self.RED)
        self.surface.blit(self.GAME_OVER_LABEL, (30, 250))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()

    def render_game_score(self, score):
        s = self.font_small.render(str(score), True, self.BLACK)
        self.surface.blit(s, (10, 560))

    def render_get_ready(self):
        self.surface.fill(self.BLUE)
        self.surface.blit(self.GET_READY_LABEL, (30, 250))
        pygame.display.update()

    def render_high_score(self, score):
        s = self.font_small.render(str(score), True, self.BLACK)
        self.surface.blit(s, (10, 10))

    def render_play_again(self):
        x = (self.surface.get_width() / 2) - \
            (self.PLAY_AGAIN_LABEL.get_width() / 2)
        self.surface.blit(self.PLAY_AGAIN_LABEL, (x, 320))
        pygame.display.update()        

    def render_sprites(self, all_sprites):
        for entity in all_sprites:
            self.surface.blit(entity.image, entity.rect)
            entity.update()

    def update(self):
        pygame.display.update()
        self.framesPerSec.tick(self.FPS)
