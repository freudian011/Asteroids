
import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField

from constants import ASTEROID_MIN_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH

from logger import log_event, log_state

from player import Player

from shot import Shot

from soundmanager import SoundManager


# Draws the player's remaining lives as small spaceships
def draw_lives(screen: pygame.Surface, lives: int) -> None:
    for i in range(lives):
        x = 35 + i * 40
        y = 65

        # Sets the direction and size of the spaceship
        forward = pygame.Vector2(0, -1)
        right = pygame.Vector2(1, 0) * 8

        # Works out the three corners of the spaceship
        a = pygame.Vector2(x, y) + forward * 12
        b = pygame.Vector2(x, y) - forward * 8 - right
        c = pygame.Vector2(x, y) - forward * 8 + right

        # Draws the spaceship on the screen
        pygame.draw.polygon(screen, "white", [a, b, c], 2)


def main() -> None:

    pygame.init()
    sound_manager = SoundManager()

    # Creates the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    # Sets up the fonts used in the game
    font = pygame.font.Font(None, 64)
    small_font = pygame.font.Font(None, 32)

    # Creates groups for objects that need to move or be drawn
    updatable: pygame.sprite.Group = pygame.sprite.Group()
    drawable: pygame.sprite.Group = pygame.sprite.Group()

    # Creates separate groups for asteroids and bullets
    asteroids: pygame.sprite.Group = pygame.sprite.Group()
    shots: pygame.sprite.Group = pygame.sprite.Group()

    # Sets up the groups that new objects will automatically join
    Asteroid.containers = (asteroids, updatable, drawable)

    Shot.containers = (shots, updatable, drawable)

    AsteroidField.containers = updatable

    # Creates the asteroid field that spawns new asteroids
    asteroid_field = AsteroidField()

    # Makes the player join the groups for moving and drawing objects
    Player.containers = (updatable, drawable)

    # Creates the player in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, sound_manager)

    dt = 0.0

    # Keeps track of the current game state
    game_over = False
    paused = False
    score = 0
    lives = 3
    player_invulnerable_timer = 0.0

    # Main game loop
    while True:

        log_state()

        # Checks for events like closing the window or pressing a key
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:

                # Pauses or resumes the game
                if not game_over and event.key == pygame.K_p:
                    paused = not paused

                # Restarts the game after game over
                if game_over and event.key == pygame.K_r:

                    # Removes all existing asteroids and shots
                    for asteroid in list(asteroids):
                        asteroid.kill()

                    for shot in list(shots):
                        shot.kill()

                    # Resets the player's position and movement
                    player.position = pygame.Vector2(
                        SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
                    )
                    player.velocity = pygame.Vector2(0, 0)
                    player.rotation = 0.0
                    player.shoot_timer = 0.0

                    # Resets the asteroid spawning timer
                    asteroid_field.spawn_timer = 0.0

                    # Resets the game statistics
                    score = 0
                    lives = 3
                    player_invulnerable_timer = 0.0

                    # Restarts the game
                    game_over = False
                    paused = False

                # Lets the player quit after the game ends
                if game_over and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        # Only updates the game while it is not paused or over
        if not game_over and not paused:

            # Updates the position of all moving objects
            updatable.update(dt)

            # Counts down the player's protection time
            player_invulnerable_timer = max(
                0, player_invulnerable_timer - dt
            )

            # Checks for collisions between asteroids, the player and bullets
            for asteroid in list(asteroids):

                # Checks if an asteroid hits the player
                if player_invulnerable_timer <= 0 and asteroid.collides_with(player):

                    log_event("player_hit")

                    lives -= 1

                    if lives <= 0:
                        game_over = True

                    else:
                        # Moves the player back to the middle of the screen
                        player.position = pygame.Vector2(
                            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
                        )

                        # Stops the player from continuing to move
                        player.velocity = pygame.Vector2(0, 0)

                    # Gives the player 1.5 seconds of protection
                    player_invulnerable_timer = 1.5

                    break

                # Checks if a bullet hits an asteroid
                for shot in list(shots):

                    if asteroid.collides_with(shot):

                        log_event("asteroid_shot")

                        # Gives points depending on the size of the asteroid
                        if asteroid.radius <= ASTEROID_MIN_RADIUS:
                            score += 100
                        elif asteroid.radius <= ASTEROID_MIN_RADIUS * 2:
                            score += 50
                        else:
                            score += 20

                        shot.kill()

                        sound_manager.play_explosion()

                        asteroid.split()

                        break

        # Clears the screen before drawing the next frame
        screen.fill("black")

        # Creates the score text using the current score
        score_text = small_font.render(
            f"{score:08d}", True, "white"
        )

        # Displays the score in the top-left corner
        screen.blit(score_text, (20, 20))

        # Displays the player's remaining lives
        draw_lives(screen, lives)

        # Draws every object in the drawable group
        for obj in drawable:

            # Makes the player flash when it is protected after being hit
            if obj == player and player_invulnerable_timer > 0:

                if int(player_invulnerable_timer * 10) % 2 == 0:
                    obj.draw(screen)

            else:
                obj.draw(screen)

        # Displays the pause screen
        if paused:

            paused_text = font.render("PAUSED", True, "white")
            resume_text = small_font.render(
                "Press P to resume", True, "white"
            )

            screen.blit(
                paused_text,
                paused_text.get_rect(
                    center=(
                        SCREEN_WIDTH / 2,
                        SCREEN_HEIGHT / 2 - 30
                    )
                )
            )

            screen.blit(
                resume_text,
                resume_text.get_rect(
                    center=(
                        SCREEN_WIDTH / 2,
                        SCREEN_HEIGHT / 2 + 30
                    )
                )
            )

        # Displays the game-over screen when the player runs out of lives
        if game_over:

            game_over_text = font.render(
                "GAME OVER", True, "white"
            )

            restart_text = small_font.render(
                "R to restart | ESC to quit", True, "white"
            )

            # Places the game-over message in the middle of the screen
            screen.blit(
                game_over_text,
                game_over_text.get_rect(
                    center=(
                        SCREEN_WIDTH / 2,
                        SCREEN_HEIGHT / 2 - 30
                    )
                )
            )

            # Displays the instructions underneath the game-over message
            screen.blit(
                restart_text,
                restart_text.get_rect(
                    center=(
                        SCREEN_WIDTH / 2,
                        SCREEN_HEIGHT / 2 + 30
                    )
                )
            )

        # Updates the screen so everything that was drawn becomes visible
        pygame.display.flip()

        # Limits the game to 60 frames per second and works out the time between frames
        dt = clock.tick(60) / 1000


# Starts the game when this file is run
if __name__ == "__main__":
    main()
