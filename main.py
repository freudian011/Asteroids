
import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField

from constants import SCREEN_HEIGHT, SCREEN_WIDTH

from logger import log_event, log_state

from player import Player

from shot import Shot

from soundmanager import SoundManager


def main() -> None:

    pygame.init()
    sound_manager = SoundManager()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    # Fonts
    font = pygame.font.Font(None, 64)
    small_font = pygame.font.Font(None, 32)

    # Sprite groups
    updatable: pygame.sprite.Group = pygame.sprite.Group()

    drawable: pygame.sprite.Group = pygame.sprite.Group()

    asteroids: pygame.sprite.Group = pygame.sprite.Group()
    shots: pygame.sprite.Group = pygame.sprite.Group()

    # Containers
    Asteroid.containers = (asteroids, updatable, drawable)

    Shot.containers = (shots, updatable, drawable)

    AsteroidField.containers = updatable

    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, sound_manager)

    dt = 0.0

    # Game state
    game_over = False

    while True:

        log_state()

        # Event handling
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:

                if game_over and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        # Update game objects only while playing
        if not game_over:

            updatable.update(dt)

            # Collision detection
            for asteroid in list(asteroids):

                # Player collision
                if asteroid.collides_with(player):

                    log_event("player_hit")

                    game_over = True

                    break

                # Shot collision
                for shot in list(shots):

                    if asteroid.collides_with(shot):

                        log_event("asteroid_shot")

                        sound_manager.play_explosion()

                        shot.kill()

                        asteroid.split()

                        break

        # Drawing
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

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

        pygame.display.flip()

        # Limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
