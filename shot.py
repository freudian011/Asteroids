
import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)
        # Inherits the position and velocity attributes from CircleShape,
        # while using SHOT_RADIUS to determine the bullet's collision size.
        # Sets up the bullet with its position and size

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        # Uses Pygame's circle drawing function to render the bullet.
        # The position determines its centre, radius determines its size,
        # and LINE_WIDTH determines the thickness of its outline.
        # Draws the bullet as a small white circle

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        # Uses the bullet's velocity and elapsed frame time (dt)
        # to calculate its movement, keeping its speed consistent
        # regardless of the game's frame rate.
        # Moves the bullet based on its speed and direction
