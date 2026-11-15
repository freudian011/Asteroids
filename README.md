# Asteroids

My Year 9 Computing Studies Project: Asteroids

A classic Asteroids arcade game built with **Python** and **Pygame**.

The objective is to survive by navigating through space, avoiding asteroids and destroying them using projectiles. Larger asteroids split into smaller ones when hit, creating an increasingly challenging environment.

## Features

- Player movement and rotation.
- Projectile shooting with a firing cooldown.
- Random asteroid spawning from the edges of the screen.
- Asteroid splitting when hit.
- Circle-based collision detection.
- Frame-rate-independent movement using delta time (`dt`).
- Object-oriented design using classes and inheritance.
- Event and game-state logging.

## Controls

| Key | Action |
|:---:|---|
| `W` | Move forward |
| `S` | Move backward |
| `A` | Rotate left |
| `D` | Rotate right |
| `SPACE` | Shoot |

## Requirements

- Python 3.13 or higher
- Pygame 2.6.1

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/freudian011/Asteroids.git
```

**2. Navigate into the project directory**

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

Run the following command from the project directory:

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
├── main.py           # Main game loop and initialisation
├── player.py         # Player movement, rotation and shooting
├── asteroid.py       # Asteroid behaviour and splitting
├── asteroidfield.py  # Asteroid spawning and positioning
├── circleshape.py    # Base class and collision detection
├── shot.py           # Projectile behaviour
├── constants.py      # Game configuration and constants
├── logger.py         # Event and game-state logging
│
├── pyproject.toml    # Project configuration and dependencies
├── uv.lock           # Locked dependency versions
└── README.md         # Project documentation
```

## Technical Concepts

This project uses several Python programming concepts:

- **Object-Oriented Programming (OOP):** Game entities are represented using individual classes.
- **Inheritance:** The `Player`, `Asteroid` and `Shot` classes inherit shared functionality from `CircleShape`.
- **Polymorphism:** Different game objects implement their own drawing and updating behaviour.
- **Pygame Sprite Groups:** Objects are organised into groups for updating, drawing and collision management.
- **Delta Time:** Movement is calculated using elapsed time to maintain consistent behaviour across different frame rates.
- **Type Annotations:** Function parameters, return values and variables use Python type hints.

## Technologies Used

- [Python](https://www.python.org/)
- [Pygame](https://www.pygame.org/)

## Author

Developed by [freudian011](https://github.com/freudian011).