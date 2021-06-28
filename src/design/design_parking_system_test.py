from unittest import TestCase
from .design_parking_system import DesignParkingSystem


class DesignParkingSystemTest(TestCase):

    def test_default_input(self):
        solution = DesignParkingSystem(1, 1, 0)

        self.assertTrue(solution.addCar(1))
        self.assertTrue(solution.addCar(2))
        self.assertFalse(solution.addCar(3))
        self.assertFalse(solution.addCar(1))
