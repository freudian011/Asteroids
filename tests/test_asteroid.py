
import pygame

import asteroid as asteroid_module
from asteroid import Asteroid
from constants import ASTEROID_MIN_RADIUS


# Tests if an asteroid is created with the correct starting values.
def test_asteroid_initialisation():
    # Creates an asteroid at position (100, 200) with a radius of 40.
    asteroid = Asteroid(100, 200, 40)

    # Checks that the asteroid starts at the correct position.
    assert asteroid.position == pygame.Vector2(100, 200)

    # Checks that the asteroid has the correct radius.
    assert asteroid.radius == 40

    # Checks that the asteroid has 10 vertices.
    assert len(asteroid.vertices) == 10


# Tests if the asteroid moves to the correct position.
def test_asteroid_movement():
    # Creates an asteroid at position (100, 200).
    asteroid = Asteroid(100, 200, 40)

    # Sets the asteroid's speed and direction.
    asteroid.velocity = pygame.Vector2(10, 20)

    # Updates the asteroid's position after 1 second.
    asteroid.update(1)

    # Checks that the asteroid has moved 10 units across and 20 units down.
    assert asteroid.position == pygame.Vector2(110, 220)


# Tests if a large asteroid splits into two smaller asteroids.
def test_asteroid_splitting(monkeypatch):
    # Creates a group to keep track of the asteroids.
    asteroids = pygame.sprite.Group()

    # Makes newly created asteroids get added to this group.
    Asteroid.containers = (asteroids,)

    # Temporarily stops log_event from doing anything during this test.
    monkeypatch.setattr(asteroid_module, "log_event", lambda event: None)

    # Creates a large asteroid with a radius three times the minimum radius.
    asteroid = Asteroid(100, 200, ASTEROID_MIN_RADIUS * 3)

    # Sets the asteroid's velocity to move horizontally.
    asteroid.velocity = pygame.Vector2(10, 0)

    # Splits the asteroid into two smaller asteroids.
    asteroid.split()

    # Checks that exactly two new asteroids were created.
    assert len(asteroids) == 2

    # Goes through each of the new asteroids.
    for new_asteroid in asteroids:
        # Checks that both new asteroids have the correct radius.
        assert new_asteroid.radius == ASTEROID_MIN_RADIUS * 2


# Tests that a small asteroid cannot split into smaller asteroids.
def test_small_asteroid_does_not_split(monkeypatch):
    # Creates a group to keep track of any new asteroids.
    asteroids = pygame.sprite.Group()

    # Makes newly created asteroids get added to this group.
    Asteroid.containers = (asteroids,)

    # Temporarily stops log_event from doing anything during this test.
    monkeypatch.setattr(asteroid_module, "log_event", lambda event: None)

    # Creates an asteroid with the minimum possible radius.
    asteroid = Asteroid(100, 200, ASTEROID_MIN_RADIUS)

    # Tries to split the asteroid.
    asteroid.split()

    # Checks that no new asteroids were created because the asteroid is too small.
    assert len(asteroids) == 0
