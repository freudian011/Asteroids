
import pygame


class SoundManager:

    def __init__(self):
        pygame.mixer.init()  # Starts the sound system

        self.shoot_sound = pygame.mixer.Sound("sounds/shoot.wav")
        self.explosion_sound = pygame.mixer.Sound("sounds/explosion.wav")
        # Loads the shooting and explosion sounds

    def play_shoot(self):
        self.shoot_sound.play()  # Plays the shooting sound

    def play_explosion(self):
        self.explosion_sound.stop()  # Stops any explosion sound already playing
        self.explosion_sound.play()  # Plays the explosion sound
