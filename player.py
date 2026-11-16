
import pygame
from circleshape import CircleShape
from constants import (
    LINE_WIDTH,
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN_SECONDS,
    PLAYER_SHOOT_SPEED,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from shot import Shot


class Player(CircleShape):
    def __init__(self, x: float, y: float, sound_manager) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0.0  # Keeps track of which way the ship is facing
        self.shoot_timer = 0.0  # Controls how often the player can shoot
        self.sound_manager = sound_manager

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
        # Draws the player's spaceship

    def triangle(self) -> list[pygame.Vector2]:
        # Creates a forward-facing vector and rotates it according to the player's rotation.
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # Works out which way the ship is pointing

        # Creates a perpendicular vector to calculate the width of the spaceship.
        # Scaling it by the radius controls how wide the ship's back corners are.
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        # Works out the direction and size of the ship's sides

        # Calculates the three vertices of the triangular spaceship using its position and direction.
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        # Finds the three corners of the spaceship

        return [a, b, c]  # Sends the three corners back

    def update(self, dt: float) -> None:
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()  # Checks which keys are being pressed

        if keys[pygame.K_w]:
            self.move(dt)  # Moves forwards
        if keys[pygame.K_s]:
            self.move(-dt)  # Moves backwards
        if keys[pygame.K_a]:
            self.rotate(-dt)  # Turns left
        if keys[pygame.K_d]:
            self.rotate(dt)  # Turns right
        if keys[pygame.K_SPACE]:
            self.shoot()  # Shoots a bullet

        self.wrap_position()  # Keeps the player on the screen by moving it to the opposite side

    def shoot(self) -> None:
        if self.shoot_timer > 0:
            return  # Stops the player from shooting too quickly

        self.shoot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS

        shot = Shot(self.position.x, self.position.y)
        # Creates a bullet where the player is

        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        # Calculates the bullet's velocity using the player's rotation and shooting speed.

        self.sound_manager.play_shoot()  # Plays the shooting sound

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt
        # Changes which way the ship is facing

    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        # Works out which direction the ship should move

        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        # Works out how far the ship should move

        self.position += rotated_with_speed_vector
        # Moves the ship

    def wrap_position(self) -> None:
        # Moves the player to the opposite side when it leaves the screen

        if self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius

        elif self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius

        if self.position.y < -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius

        elif self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius
