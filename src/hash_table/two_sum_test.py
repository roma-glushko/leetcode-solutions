from unittest import TestCase, main

from .two_sum import Solution


class TestIslandPerimeter(TestCase):

    def test_default_grid(self):
        solution = Solution()
        perimeter = solution.twoSum(
            [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
        )

        self.assertEqual(perimeter, 16)

    def test_single_land_cell_grid(self):
        solution = Solution()
        perimeter = solution.islandPerimeter([[1]])

        self.assertEqual(perimeter, 4)

    def test_land_and_water_in_single_row(self):
        solution = Solution()
        perimeter = solution.islandPerimeter([[1, 0]])

        self.assertEqual(perimeter, 4)
