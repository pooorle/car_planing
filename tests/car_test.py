from classes import Car
import pytest


def test_car_update():
    car = Car(0, 0, angle=0, length=2, max_steering=80, max_acceleration=4.0)
    car.acceleration = 2.0
    car.steering = 30.0
    dt = 1.0
    car.update(dt)
    assert car.position == (car.max_velocity * dt, 0)
    assert car.angle == 15.0


def test_car_max_velocity():
    car = Car(0, 0, angle=0, length=2, max_steering=80, max_acceleration=4.0)
    assert car.max_velocity == 5


def test_car_brake_deceleration():
    car = Car(0, 0, angle=0, length=2, max_steering=80, max_acceleration=4.0)
    assert car.brake_deceleration == 4


def test_car_free_deceleration():
    car = Car(0, 0, angle=0, length=2, max_steering=80, max_acceleration=4.0)
    assert car.free_deceleration == 1


pytest.main(["-v", "--html=report_car.html"])
