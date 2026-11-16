
import pygame

import asteroid as asteroid_module
from asteroid import Asteroid
from constants import ASTEROID_MIN_RADIUS


def test_asteroid_initialisation():
    asteroid = Asteroid(100, 200, 40)

    assert asteroid.position == pygame.Vector2(100, 200)
    assert asteroid.radius == 40
    assert len(asteroid.vertices) == 10


def test_asteroid_movement():
    asteroid = Asteroid(100, 200, 40)
    asteroid.velocity = pygame.Vector2(10, 20)

    asteroid.update(1)

    assert asteroid.position == pygame.Vector2(110, 220)


def test_asteroid_splitting(monkeypatch):
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids,)

    monkeypatch.setattr(asteroid_module, "log_event", lambda event: None)

    asteroid = Asteroid(100, 200, ASTEROID_MIN_RADIUS * 3)
    asteroid.velocity = pygame.Vector2(10, 0)

    asteroid.split()

    assert len(asteroids) == 2

    for new_asteroid in asteroids:
        assert new_asteroid.radius == ASTEROID_MIN_RADIUS * 2


def test_small_asteroid_does_not_split(monkeypatch):
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids,)

    monkeypatch.setattr(asteroid_module, "log_event", lambda event: None)

    asteroid = Asteroid(100, 200, ASTEROID_MIN_RADIUS)
    asteroid.split()

    assert len(asteroids) == 0
