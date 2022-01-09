import pygame


class Sound():
    def __init__(self):
        # game sounds
        self.crash_sound = pygame.mixer.Sound('assets/crash.wav')
        self.backgroud_music = pygame.mixer.Sound('assets/Action-Rock.mp3')
        self.current_music = None

    def play_backgroud_music(self):
        self.current_music = self.backgroud_music.play()

    def play_crash(self):
        self.crash_sound.play()

    def stop(self):
        if self.current_music != None:
            self.current_music.stop()
