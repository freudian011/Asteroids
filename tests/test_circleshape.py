
import pygame

from circleshape import CircleShape


def test_circleshape_initialisation():
    circle = CircleShape(100, 200, 30)

    assert circle.position == pygame.Vector2(100, 200)
    assert circle.radius == 30
    assert circle.velocity == pygame.Vector2(0, 0)


def test_collision():
    circle1 = CircleShape(100, 100, 30)
    circle2 = CircleShape(120, 100, 30)

    assert circle1.collides_with(circle2) == True


def test_no_collision():
    circle1 = CircleShape(100, 100, 20)
    circle2 = CircleShape(200, 200, 20)

    assert circle1.collides_with(circle2) == False


def test_touching_collision():
    circle1 = CircleShape(100, 100, 20)
    circle2 = CircleShape(140, 100, 20)

    assert circle1.collides_with(circle2) == True
