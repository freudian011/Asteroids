import random

import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
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
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)
        # Sends the two new asteroids in slightly different directions

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(
            self.position.x, self.position.y, new_radius
        )
        asteroid_one.velocity = a * 1.2

        asteroid_two = Asteroid(
            self.position.x, self.position.y, new_radius
        )
        asteroid_two.velocity = b * 1.2