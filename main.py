
import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField

from constants import SCREEN_HEIGHT, SCREEN_WIDTH

from logger import log_event, log_state

from player import Player

from shot import Shot

from soundmanager import SoundManager


def main() -> None:

    pygame.init()  # Starts Pygame
    sound_manager = SoundManager()  # Handles the game's sounds

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()  # Keeps track of time between frames

    # Fonts
    font = pygame.font.Font(None, 64)
    small_font = pygame.font.Font(None, 32)

    # Sprite groups
    updatable: pygame.sprite.Group = pygame.sprite.Group()
    drawable: pygame.sprite.Group = pygame.sprite.Group()

    asteroids: pygame.sprite.Group = pygame.sprite.Group()
    shots: pygame.sprite.Group = pygame.sprite.Group()

    # Containers
    # Automatically adds new objects to the correct sprite groups
    Asteroid.containers = (asteroids, updatable, drawable)

    Shot.containers = (shots, updatable, drawable)

    AsteroidField.containers = updatable

    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, sound_manager)
    # Creates the player in the middle of the screen

    dt = 0.0

    # Game state
    game_over = False  # Tracks whether the game has ended

    while True:

        log_state()  # Records the current game state

        # Event handling
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return  # Closes the game

            if event.type == pygame.KEYDOWN:

                if game_over and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return  # Allows the player to quit after losing

        # Update game objects only while playing
        if not game_over:

            updatable.update(dt)  # Updates all objects that can move

            # Collision detection
            for asteroid in list(asteroids):

                # Player collision
                if asteroid.collides_with(player):

                    log_event("player_hit")

                    game_over = True

                    break  # Stops checking asteroids once the player is hit

                # Shot collision
                for shot in list(shots):

                    if asteroid.collides_with(shot):

                        log_event("asteroid_shot")

                        sound_manager.play_explosion()

                        shot.kill()  # Removes the shot after hitting an asteroid

                        asteroid.split()  # Splits the asteroid into smaller ones

                        break

        # Drawing
        screen.fill("black")  # Clears the screen before drawing the next frame

        for obj in drawable:
            obj.draw(screen)  # Draws every visible game object

        # Game Over screen
        if game_over:

            game_over_text = font.render(
                "GAME OVER", True, "white"
            )

            restart_text = small_font.render(
                "Press ESC to quit", True, "white"
            )

            screen.blit(
                game_over_text,
                game_over_text.get_rect(
                    center=(
                        SCREEN_WIDTH / 2,
                        SCREEN_HEIGHT / 2 - 30
                    )
                )
            )

            screen.blit(
                restart_text,
                restart_text.get_rect(
                    center=(
                        SCREEN_WIDTH / 2,
                        SCREEN_HEIGHT / 2 + 30
                    )
                )
            )

        pygame.display.flip()  # Displays everything drawn this frame

        # Limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
