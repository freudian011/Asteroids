
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


# Creates groups to store the asteroid fields and asteroids for testing.
@pytest.fixture
def asteroid_groups(monkeypatch):
    # Creates separate sprite groups for the fields and asteroids.
    field_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    # Temporarily sets the containers for both classes to the test groups.
    monkeypatch.setattr(AsteroidField, "containers", field_group, raising=False)
    monkeypatch.setattr(Asteroid, "containers", (asteroid_group,), raising=False)

    # Returns both groups so the tests can use them.
    return field_group, asteroid_group


# Tests if the asteroid field is created with the correct starting values.
def test_asteroidfield_initialisation(asteroid_groups):
    # Creates a new asteroid field.
    field = AsteroidField()

    # Checks that the spawn timer starts at 0.
    assert field.spawn_timer == 0.0


# Tests if an asteroid can be spawned with the correct position and movement.
def test_asteroid_spawn(asteroid_groups):
    # Creates a new asteroid field.
    field = AsteroidField()

    # Gets the asteroid group from the fixture.
    _, asteroids = asteroid_groups

    # Sets the starting position and velocity for the asteroid.
    position = pygame.Vector2(100, 200)
    velocity = pygame.Vector2(50, 0)

    # Spawns an asteroid using the position and velocity above.
    field.spawn(40, position, velocity)

    # Checks that exactly one asteroid was added to the group.
    assert len(asteroids) == 1

    # Gets the asteroid that was just created.
    asteroid = asteroids.sprites()[0]

    # Checks that the asteroid has the correct position.
    assert asteroid.position == position

    # Checks that the asteroid has the correct radius.
    assert asteroid.radius == 40

    # Checks that the asteroid has the correct velocity.
    assert asteroid.velocity == velocity


# Tests if the spawn timer counts up correctly over time.
def test_spawn_timer(asteroid_groups):
    # Creates a new asteroid field.
    field = AsteroidField()

    # Gets the asteroid group from the fixture.
    _, asteroids = asteroid_groups

    # Updates the field using half of the normal spawn time.
    field.update(ASTEROID_SPAWN_RATE_SECONDS / 2)

    # Checks that no asteroids have spawned yet.
    assert len(asteroids) == 0

    # Checks that the timer has increased by half the spawn time.
    assert field.spawn_timer == ASTEROID_SPAWN_RATE_SECONDS / 2


# Tests if asteroids spawn automatically after the spawn timer runs out.
def test_automatic_asteroid_spawn(asteroid_groups, monkeypatch):
    # Creates a new asteroid field.
    field = AsteroidField()

    # Gets the asteroid group from the fixture.
    _, asteroids = asteroid_groups

    # Makes the random edge selection always choose the first edge.
    # This makes the test predictable instead of choosing a random edge.
    monkeypatch.setattr(
        "asteroidfield.random.choice",
        lambda edges: edges[0]
    )

    # Sets the random numbers that will be used during this test.
    random_values = iter([50, 0, 1])

    # Replaces the random number generator with the values above.
    monkeypatch.setattr(
        "asteroidfield.random.randint",
        lambda a, b: next(random_values)
    )

    # Makes the random decimal value always be 0.5.
    monkeypatch.setattr(
        "asteroidfield.random.uniform",
        lambda a, b: 0.5
    )

    # Updates the field for slightly longer than the spawn rate.
    field.update(ASTEROID_SPAWN_RATE_SECONDS + 0.1)

    # Checks that exactly one asteroid has spawned.
    assert len(asteroids) == 1

    # Gets the asteroid that was created.
    asteroid = asteroids.sprites()[0]

    # Checks that the asteroid has the minimum radius.
    assert asteroid.radius == ASTEROID_MIN_RADIUS

    # Checks that the asteroid starts just outside the left side of the screen.
    assert asteroid.position.x == -ASTEROID_MAX_RADIUS

    # Checks that the asteroid spawns halfway down the screen.
    assert asteroid.position.y == SCREEN_HEIGHT * 0.5

    # Checks that the asteroid moves at the expected speed and direction.
    assert asteroid.velocity == pygame.Vector2(50, 0)

    # Checks that the spawn timer resets to 0 after an asteroid spawns.
    assert field.spawn_timer == 0
