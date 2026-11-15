
import pygame


class SoundManager:

    def __init__(self):
        pygame.mixer.init()

        self.shoot_sound = pygame.mixer.Sound("sounds/shoot.wav")
        self.explosion_sound = pygame.mixer.Sound("sounds/explosion.wav")

    def play_shoot(self):
        self.shoot_sound.play()

    def play_explosion(self):
        self.explosion_sound.stop()
        self.explosion_sound.play()
