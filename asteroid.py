
import random

import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


# Asteroid inherits from CircleShape, so it can use its position, radius and velocity.
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        # Calls the CircleShape constructor to set up the asteroid's basic properties.
        super().__init__(x, y, radius)

        # Generate the asteroid's irregular shape
        self.vertices = []  # Stores the points that make up the asteroid

        for i in range(10):
            angle = i * 360 / 10  # Spreads 10 points evenly around a circle

            direction = pygame.Vector2(1, 0).rotate(angle)
            # Creates a direction for each point

            distance = radius * random.uniform(0.8, 1.2)
            # Gives each point a slightly random distance from the centre

            self.vertices.append(direction * distance)
            # Adds the new point to the list

    def draw(self, screen: pygame.Surface) -> None:
        points = [
            self.position + vertex
            for vertex in self.vertices
        ]
        # Gets the actual screen position of each point

        pygame.draw.polygon(screen, "white", points, LINE_WIDTH)
        # Connects all the points to draw the asteroid

    def update(self, dt: float) -> None:
        # Moves the asteroid based on its velocity and the time passed.
        self.position += self.velocity * dt

    def split(self) -> None:
        # Removes the original asteroid from its sprite groups.
        self.kill()

        # Stops the asteroid from splitting if it is already at the minimum size.
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Records that an asteroid has been split.
        log_event("asteroid_split")

        # Chooses a random angle to change the direction of the new asteroids.
        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)
        # Sends the two new asteroids in slightly different directions

        # Makes the new asteroids smaller than the original one.
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Creates the first new asteroid at the original asteroid's position.
        asteroid_one = Asteroid(
            self.position.x, self.position.y, new_radius
        )
        # Gives the first asteroid its new velocity.
        asteroid_one.velocity = a * 1.2

        # Creates the second new asteroid at the same position.
        asteroid_two = Asteroid(
            self.position.x, self.position.y, new_radius
        )
        # Gives the second asteroid its new velocity.
        asteroid_two.velocity = b * 1.2
