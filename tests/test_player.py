
import pygame
from unittest.mock import MagicMock

from player import Player
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED, PLAYER_SHOOT_SPEED


def test_player_initialisation():
    player = Player(100, 200, MagicMock())

    assert player.position == pygame.Vector2(100, 200)
    assert player.radius == PLAYER_RADIUS
    assert player.rotation == 0.0
    assert player.shoot_timer == 0.0


def test_player_rotation():
    player = Player(100, 200, MagicMock())

    player.rotate(1)

    assert player.rotation == PLAYER_TURN_SPEED


def test_player_movement():
    player = Player(100, 200, MagicMock())

    player.move(1)

    assert player.position == pygame.Vector2(100, 200 + PLAYER_SPEED)


def test_player_shooting():
    shots = pygame.sprite.Group()
    Shot.containers = (shots,)

    sound_manager = MagicMock()
    player = Player(100, 200, sound_manager)

    player.shoot()

    assert len(shots) == 1

    shot = shots.sprites()[0]

    assert shot.position == player.position
    assert shot.velocity == pygame.Vector2(0, PLAYER_SHOOT_SPEED)
    sound_manager.play_shoot.assert_called_once()


def test_player_cooldown():
    shots = pygame.sprite.Group()
    Shot.containers = (shots,)

    sound_manager = MagicMock()
    player = Player(100, 200, sound_manager)

    player.shoot_timer = 1.0
    player.shoot()

    assert len(shots) == 0
    sound_manager.play_shoot.assert_not_called()
