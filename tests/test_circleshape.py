
import pygame

from circleshape import CircleShape


# Tests if a CircleShape object is created with the correct starting values.
def test_circleshape_initialisation():
    # Creates a circle at position (100, 200) with a radius of 30.
    circle = CircleShape(100, 200, 30)

    # Checks that the circle starts at the correct position.
    assert circle.position == pygame.Vector2(100, 200)

    # Checks that the circle has the correct radius.
    assert circle.radius == 30

    # Checks that the circle's velocity starts at 0 because it is not moving.
    assert circle.velocity == pygame.Vector2(0, 0)


# Tests if the collision detection works when two circles overlap.
def test_collision():
    # Creates two circles that overlap each other.
    circle1 = CircleShape(100, 100, 30)
    circle2 = CircleShape(120, 100, 30)

    # Checks that the program detects a collision between the two circles.
    assert circle1.collides_with(circle2) == True


# Tests if the program correctly detects when two circles are not touching.
def test_no_collision():
    # Creates two circles that are far apart from each other.
    circle1 = CircleShape(100, 100, 20)
    circle2 = CircleShape(200, 200, 20)

    # Checks that the program does not detect a collision.
    assert circle1.collides_with(circle2) == False


# Tests if the collision detection works when two circles are exactly touching.
def test_touching_collision():
    # Creates two circles that are touching at their edges.
    circle1 = CircleShape(100, 100, 20)
    circle2 = CircleShape(140, 100, 20)

    # Checks that touching circles are counted as a collision.
    assert circle1.collides_with(circle2) == True
