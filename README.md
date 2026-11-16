# Asteroids

My Year 9 Computing Studies Project: Asteroids

A classic Asteroids arcade game made using **Python** and **Pygame**.

The aim of the game is to survive for as long as possible by flying around space, avoiding asteroids and shooting them with projectiles. When an asteroid is hit, it splits into smaller asteroids, making the game more challenging as you play.

## Features

- Player movement and rotation.
- Shooting projectiles with a firing cooldown.
- Random asteroid spawning from the edges of the screen.
- Asteroids split into smaller pieces when hit.
- Collision detection between the player, asteroids and projectiles.
- Three lives, shown as small spaceship icons in the top-left corner.
- Player flashes when temporarily invulnerable after being hit.
- Score system that gives different points depending on asteroid size.
- Sound effects for shooting and destroying asteroids.
- Frame-rate-independent movement using delta time (`dt`).
- Object-oriented programming using classes and inheritance.
- Event and game-state logging.

## Controls

| Key | Action |
|:---:|---|
| `W` | Move forward |
| `S` | Move backward |
| `A` | Rotate left |
| `D` | Rotate right |
| `SPACE` | Shoot |

## Scoring System

You earn points by destroying asteroids. Smaller asteroids are worth more points because they can be harder to hit.

| Asteroid Size | Points |
|---|---:|
| Large | 20 |
| Medium | 50 |
| Small | 100 |

## Requirements

- Python 3.13 or higher
- Pygame 2.6.1

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/freudian011/Asteroids.git
```

**2. Navigate into the project folder**

```bash
cd Asteroids
```

**3. Install the dependencies**

```bash
pip install pygame==2.6.1
```

Alternatively, if you have [uv](https://docs.astral.sh/uv/) installed:

```bash
uv sync
```

## Running the Game

Run the following command from the project folder:

```bash
python main.py
```

If you are using `uv`, run:

```bash
uv run main.py
```

## Project Structure

```text
Asteroids/
│
├── main.py           # Main game loop and setup
├── player.py         # Player movement, rotation and shooting
├── asteroid.py       # Asteroid behaviour and splitting
├── asteroidfield.py  # Spawning asteroids
├── circleshape.py    # Base class and collision detection
├── shot.py           # Projectile behaviour
├── constants.py      # Game settings and values
├── logger.py         # Event and game-state logging
├── soundmanager.py   # Handles the game's sound effects
│
├── sounds/           # Sound effect files
├── pyproject.toml    # Project configuration and dependencies
├── uv.lock           # Locked dependency versions
└── README.md         # Project documentation
```

## Technologies Used

- [Python](https://www.python.org/)
- [Pygame](https://www.pygame.org/)

## Author

Developed by [freudian011](https://github.com/freudian011) as part of my Year 9 Computing Studies project.