from .design_parking_system import DesignParkingSystem


def test_default_input():
    solution = DesignParkingSystem(1, 1, 0)
    assert solution.addCar(1)
    assert solution.addCar(2)
    assert not solution.addCar(3)
    assert not solution.addCar(1)
