
import pygame

from shot import Shot
from constants import SHOT_RADIUS


def test_shot_initialisation():
    shot = Shot(100, 200)

    assert shot.position == pygame.Vector2(100, 200)
    assert shot.radius == SHOT_RADIUS
    assert shot.velocity == pygame.Vector2(0, 0)


def test_shot_movement():
    shot = Shot(100, 200)
    shot.velocity = pygame.Vector2(10, 20)

    shot.update(1)

    assert shot.position == pygame.Vector2(110, 220)


def test_shot_movement_with_time():
    shot = Shot(100, 200)
    shot.velocity = pygame.Vector2(10, 20)

    shot.update(0.5)

    assert shot.position == pygame.Vector2(105, 210)
