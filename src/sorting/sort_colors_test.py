from typing import List
from unittest import TestCase

from src.sorting.sort_colors import SortColors


class SortColorsTest(TestCase):
    def test_default_input(self):
        solution = SortColors()

        colors: List[int] = [2, 0, 2, 1, 1, 0]
        solution.sortColors(colors)

        self.assertEqual(
            [0, 0, 1, 1, 2, 2],
            colors,
        )

        colors: List[int] = [2, 0, 1]
        solution.sortColors(colors)

        self.assertEqual(
            [0, 1, 2],
            colors,
        )

        colors: List[int] = [0]
        solution.sortColors(colors)

        self.assertEqual(
            [0],
            colors,
        )

        colors: List[int] = [1]
        solution.sortColors(colors)

        self.assertEqual(
            [1],
            colors,
        )
