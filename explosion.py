
import math
import random

import pygame


# Represents one individual particle in an explosion
class Particle:

    def __init__(self, position):

        # Sets the particle's starting position
        self.position = pygame.Vector2(position)

        # Gives the particle a random direction
        angle = random.uniform(0, math.tau)

        # Gives the particle a random movement speed
        speed = random.uniform(50, 150)

        # Calculates the particle's velocity using its direction and speed
        self.velocity = pygame.Vector2(
            math.cos(angle), math.sin(angle)
        ) * speed

        # Sets how long the particle stays visible
        self.lifetime = 0.5

        # Gives the particle a random size
        self.radius = random.randint(2, 4)

    # Updates the particle's position and remaining lifetime
    def update(self, dt):

        # Moves the particle according to its velocity
        self.position += self.velocity * dt

        # Reduces the particle's remaining lifetime
        self.lifetime -= dt

    # Draws the particle onto the screen
    def draw(self, screen):

        # Only draws the particle while it is still alive
        if self.lifetime > 0:

            pygame.draw.circle(
                screen,
                "white",
                (int(self.position.x), int(self.position.y)),
                self.radius,
            )


# Represents a complete explosion made up of multiple particles
class Explosion:

    def __init__(self, position, particle_count=20):

        # Creates the specified number of particles at the explosion's position
        # Defaults to 20 particles if no number is provided
        self.particles = [
            Particle(position) for _ in range(particle_count)
        ]

    # Updates every particle in the explosion
    def update(self, dt):

        for particle in self.particles:
            particle.update(dt)

    # Draws every particle in the explosion
    def draw(self, screen):

        for particle in self.particles:
            particle.draw(screen)

    # Checks whether every particle has finished its animation
    def is_finished(self):

        return all(
            particle.lifetime <= 0 for particle in self.particles
        )
