
import pygame
from unittest.mock import MagicMock

from player import Player
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED, PLAYER_SHOOT_SPEED


# Tests if the player is created with the correct starting values.
def test_player_initialisation():
    # Creates a player at position (100, 200) and uses a mock sound manager.
    player = Player(100, 200, MagicMock())

    # Checks that the player starts at the correct position.
    assert player.position == pygame.Vector2(100, 200)

    # Checks that the player has the correct radius.
    assert player.radius == PLAYER_RADIUS

    # Checks that the player's rotation starts at 0 degrees.
    assert player.rotation == 0.0

    # Checks that the shooting timer starts at 0.
    assert player.shoot_timer == 0.0


# Tests if the player rotates in the correct direction and at the correct speed.
def test_player_rotation():
    # Creates a new player with a mock sound manager.
    player = Player(100, 200, MagicMock())

    # Rotates the player for 1 second.
    player.rotate(1)

    # Checks that the rotation has changed by the correct amount.
    assert player.rotation == PLAYER_TURN_SPEED


# Tests if the player moves forward in the direction they are facing.
def test_player_movement():
    # Creates a new player at position (100, 200).
    player = Player(100, 200, MagicMock())

    # Moves the player for 1 second.
    player.move(1)

    # Checks that the player has moved down by the correct speed.
    assert player.position == pygame.Vector2(100, 200 + PLAYER_SPEED)


# Tests if the player can shoot a projectile.
def test_player_shooting():
    # Creates a group to store the projectiles.
    shots = pygame.sprite.Group()

    # Makes newly created shots automatically get added to this group.
    Shot.containers = (shots,)

    # Creates a mock sound manager so no actual sound needs to play during testing.
    sound_manager = MagicMock()

    # Creates a new player using the mock sound manager.
    player = Player(100, 200, sound_manager)

    # Makes the player shoot a projectile.
    player.shoot()

    # Checks that exactly one projectile was created.
    assert len(shots) == 1

    # Gets the projectile that was created.
    shot = shots.sprites()[0]

    # Checks that the projectile starts at the player's position.
    assert shot.position == player.position

    # Checks that the projectile has the correct shooting speed and direction.
    assert shot.velocity == pygame.Vector2(0, PLAYER_SHOOT_SPEED)

    # Checks that the shooting sound was played exactly once.
    sound_manager.play_shoot.assert_called_once()


# Tests if the shooting cooldown stops the player from shooting too quickly.
def test_player_cooldown():
    # Creates a group to store any projectiles.
    shots = pygame.sprite.Group()

    # Makes newly created shots automatically get added to this group.
    Shot.containers = (shots,)

    # Creates a mock sound manager to use during the test.
    sound_manager = MagicMock()

    # Creates a new player.
    player = Player(100, 200, sound_manager)

    # Sets the shooting timer to 1 second to simulate an active cooldown.
    player.shoot_timer = 1.0

    # Tries to make the player shoot while the cooldown is active.
    player.shoot()

    # Checks that no projectile was created because the player is still on cooldown.
    assert len(shots) == 0

    # Checks that the shooting sound was not played.
    sound_manager.play_shoot.assert_not_called()
