
import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)
        # Sets up the bullet with its position and size

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        # Draws the bullet as a small white circle

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        # Moves the bullet based on its speed and direction
