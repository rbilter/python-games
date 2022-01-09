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

        # user event
        self.INC_SPEED = pygame.USEREVENT + 1
        pygame.time.set_timer(self.INC_SPEED, 1000)

    def check_events(self):
        quit = False
        for event in pygame.event.get():
            if event.type == self.INC_SPEED:
                self.E1.increment_speed()
            if event.type == QUIT:
                quit = True
        return quit

    def get_speed(self):
        return self.SCORE

    def get_player(self):
        return self.P1

    def get_ememy(self):
        return self.E1

    def had_collision(self):
        return pygame.sprite.spritecollideany(self.P1, self.enemies)

    def new_game_surface(self):
        self.surface = pygame.display.set_mode((400, 600))
        pygame.display.set_caption("Crazy Cars")

    def quit(self):
        pygame.quit()

    def render_backgroud(self):
        self.surface.blit(self.background, (0, 0))

    def render_collision(self):
        x = self.P1.rect.centerx - (self.collision.get_width() / 2)
        y = self.P1.rect.top - (self.collision.get_height() / 2)
        self.surface.blit(self.collision, (x, y))
        pygame.display.update()
        pygame.mixer.Sound('assets/crash.wav').play()

    def render_game_over(self):
        self.surface.fill(self.RED)
        self.surface.blit(self.GAME_OVER_LABEL, (30, 250))
        pygame.display.update()

        for entity in self.all_sprites:
            entity.kill()

    def render_sprites(self):
        for entity in self.all_sprites:
            self.surface.blit(entity.image, entity.rect)
            entity.update()

    def render_game_score(self, score):
        s = self.font_small.render(str(score), True, self.BLACK)
        self.surface.blit(s, (10, 560))

    def render_high_score(self, score):
        s = self.font_small.render(str(score), True, self.BLACK)
        self.surface.blit(s, (10, 10))

    def start_game(self):
        self.SPEED = 5
        self.SCORE = 0

        self.P1 = players.Player(self.SCREEN_WIDTH)
        self.E1 = players.Enemy(self.SCREEN_WIDTH, self.SPEED)

        self.enemies = pygame.sprite.Group()
        self.enemies.add(self.E1)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.P1)
        self.all_sprites.add(self.E1)

        self.surface.fill(self.BLUE)
        self.surface.blit(self.GET_READY_LABEL, (30, 250))
        pygame.display.update()

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

            if not key_pressed:
                x = (self.surface.get_width() / 2) - \
                    (self.PLAY_AGAIN_LABEL.get_width() / 2)
                self.surface.blit(self.PLAY_AGAIN_LABEL, (x, 320))
                pygame.display.update()
            else:
                break
        return try_again

    def update(self):
        pygame.display.update()
        self.framesPerSec.tick(self.FPS)
