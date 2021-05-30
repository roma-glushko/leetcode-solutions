from unittest import TestCase

from .number_of_islands import NumberOfIslands


class NumberOfIslandsTest(TestCase):

    def test_big_island(self):
        solution = NumberOfIslands()
        num_of_islands = solution.numIslands([
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ])

        self.assertEqual(num_of_islands, 1)

    def test_three_islands(self):
        solution = NumberOfIslands()
        area = solution.numIslands([
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ])

        self.assertEqual(area, 3)

    def test_no_islands(self):
        solution = NumberOfIslands()
        area = solution.numIslands([
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ])

        self.assertEqual(area, 0)

    def test_one_huge_island(self):
        solution = NumberOfIslands()
        area = solution.numIslands([
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"]
        ])

        self.assertEqual(area, 1)
