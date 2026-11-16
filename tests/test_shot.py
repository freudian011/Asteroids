
import pygame

from shot import Shot
from constants import SHOT_RADIUS


# Tests if a shot is created with the correct starting values.
def test_shot_initialisation():
    # Creates a shot at position (100, 200).
    shot = Shot(100, 200)

    # Checks that the shot starts at the correct position.
    assert shot.position == pygame.Vector2(100, 200)

    # Checks that the shot has the correct radius.
    assert shot.radius == SHOT_RADIUS

    # Checks that the shot's velocity starts at 0 because it is not moving yet.
    assert shot.velocity == pygame.Vector2(0, 0)


# Tests if a shot moves to the correct position based on its velocity.
def test_shot_movement():
    # Creates a shot at position (100, 200).
    shot = Shot(100, 200)

    # Sets the shot's velocity to 10 units horizontally and 20 vertically.
    shot.velocity = pygame.Vector2(10, 20)

    # Updates the shot's position after 1 second.
    shot.update(1)

    # Checks that the shot has moved to position (110, 220).
    assert shot.position == pygame.Vector2(110, 220)


# Tests if the shot moves the correct distance when less than 1 second passes.
def test_shot_movement_with_time():
    # Creates a shot at position (100, 200).
    shot = Shot(100, 200)

    # Sets the shot's velocity to 10 units horizontally and 20 vertically.
    shot.velocity = pygame.Vector2(10, 20)

    # Updates the shot's position after half a second.
    shot.update(0.5)

    # Checks that the shot has moved half the distance compared to 1 second.
    assert shot.position == pygame.Vector2(105, 210)
