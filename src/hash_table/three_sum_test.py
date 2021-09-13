from unittest import TestCase

from .three_sum import ThreeSum


class ThreeSumTest(TestCase):
    def test_base_input(self):
        solution = ThreeSum()

        self.assertCountEqual(
            [(-1, -1, 2), (-1, 0, 1)], solution.threeSum2([-1, 0, 1, 2, -1, -4])
        )

    def test_empty_case(self):
        solution = ThreeSum()

        self.assertCountEqual([], solution.threeSum([]))

    def test_too_little_elements_case(self):
        solution = ThreeSum()

        self.assertCountEqual([], solution.threeSum([0]))

        self.assertCountEqual([], solution.threeSum([1, -1]))
