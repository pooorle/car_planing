import pytest
from classes import Target, Car, Vector2


def test_target_creation():
    target = Target(5, 10)
    assert target.position == Vector2(5, 10)
    assert target.passed is False
    assert target.alpha == 0
    assert target.visible is False


def test_target_passed():
    target = Target(5, 10)
    car = Car(5, 20)
    target.update(car, 1, 0)
    assert target.passed is True
    target.position = Vector2(5, 19)
    target.update(car, 1, 0)
    assert target.passed is True
    assert target.visible is False


def test_target_visible():
    target = Target(5, 10)
    car = Car(5, 20)
    target.update(car, 1, 0)
    assert target.visible is False
    target.position = Vector2(5, 21)
    target.update(car, 1, 0)
    assert target.visible is False
    target.position = Vector2(5, 22)
    target.update(car, 1, 0)
    assert target.visible is False


def test_target_angle():
    target = Target(5, 10)
    car = Car(5, 20)
    target.update(car, 1, 0)
    target.position = Vector2(6, 21)
    target.update(car, 1, 0)
    assert target.alpha == -45
    target.position = Vector2(4, 21)
    target.update(car, 1, 0)
    assert target.alpha == -135


pytest.main(["-v", "--html=report_target.html"])
