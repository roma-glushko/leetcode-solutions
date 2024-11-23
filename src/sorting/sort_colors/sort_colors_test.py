from unittest import TestCase

from src.sorting.sort_colors import SortColors


class SortColorsTest(TestCase):
    def test_default_input(self):
        solution = SortColors()

        colors: list[int] = [2, 0, 2, 1, 1, 0]
        solution.sortColors(colors)

        self.assertEqual(
            [0, 0, 1, 1, 2, 2],
            colors,
        )

        colors = [2, 0, 1]
        solution.sortColors(colors)

        self.assertEqual(
            [0, 1, 2],
            colors,
        )

        colors = [0]
        solution.sortColors(colors)

        self.assertEqual(
            [0],
            colors,
        )

        colors = [1]
        solution.sortColors(colors)

        self.assertEqual(
            [1],
            colors,
        )
