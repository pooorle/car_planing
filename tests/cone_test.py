import pytest
from classes import Cone, Car


def test_cone_init():
    c = Cone(10, 20, "left")
    assert c.position.x == 10
    assert c.position.y == 20
    assert c.category == "left"
    assert c.alpha is None
    assert c.dist_car is None
    assert c.visible is False


def test_cone_update_visible():
    c = Cone(10, 20, "left")
    car = Car(0, 0, angle=0)
    car.fov = 100
    car.auto = True
    car.position = (5, 0)
    car_angle = 0
    ppu = 1

    c.update(car, ppu, car_angle)

    assert c.dist_car == 5
    assert c.visible is True


def test_cone_update_not_visible():
    c = Cone(10, 20, "left")
    car = Car(0, 0, angle=0)
    car.fov = 100
    car.auto = True
    car.position = (100, 0)
    car_angle = 0
    ppu = 1

    c.update(car, ppu, car_angle)

    assert c.dist_car == 100
    assert c.visible is False


pytest.main(["-v", "--html=report_cone.html"])
