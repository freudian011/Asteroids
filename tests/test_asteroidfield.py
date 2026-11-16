
import pygame
import pytest

from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import (
    ASTEROID_MIN_RADIUS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_SPAWN_RATE_SECONDS,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)


@pytest.fixture
def asteroid_groups(monkeypatch):
    field_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    monkeypatch.setattr(AsteroidField, "containers", field_group, raising=False)
    monkeypatch.setattr(Asteroid, "containers", (asteroid_group,), raising=False)

    return field_group, asteroid_group


def test_asteroidfield_initialisation(asteroid_groups):
    field = AsteroidField()

    assert field.spawn_timer == 0.0


def test_asteroid_spawn(asteroid_groups):
    field = AsteroidField()
    _, asteroids = asteroid_groups

    position = pygame.Vector2(100, 200)
    velocity = pygame.Vector2(50, 0)

    field.spawn(40, position, velocity)

    assert len(asteroids) == 1

    asteroid = asteroids.sprites()[0]

    assert asteroid.position == position
    assert asteroid.radius == 40
    assert asteroid.velocity == velocity


def test_spawn_timer(asteroid_groups):
    field = AsteroidField()
    _, asteroids = asteroid_groups

    field.update(ASTEROID_SPAWN_RATE_SECONDS / 2)

    assert len(asteroids) == 0
    assert field.spawn_timer == ASTEROID_SPAWN_RATE_SECONDS / 2


def test_automatic_asteroid_spawn(asteroid_groups, monkeypatch):
    field = AsteroidField()
    _, asteroids = asteroid_groups

    monkeypatch.setattr(
        "asteroidfield.random.choice",
        lambda edges: edges[0]
    )

    random_values = iter([50, 0, 1])

    monkeypatch.setattr(
        "asteroidfield.random.randint",
        lambda a, b: next(random_values)
    )

    monkeypatch.setattr(
        "asteroidfield.random.uniform",
        lambda a, b: 0.5
    )

    field.update(ASTEROID_SPAWN_RATE_SECONDS + 0.1)

    assert len(asteroids) == 1

    asteroid = asteroids.sprites()[0]

    assert asteroid.radius == ASTEROID_MIN_RADIUS
    assert asteroid.position.x == -ASTEROID_MAX_RADIUS
    assert asteroid.position.y == SCREEN_HEIGHT * 0.5
    assert asteroid.velocity == pygame.Vector2(50, 0)
    assert field.spawn_timer == 0
