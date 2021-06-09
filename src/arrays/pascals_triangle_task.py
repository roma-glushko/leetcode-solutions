from unittest import TestCase

from .pascals_triangle import PascalsTriangle


class PascalsTriangleTask(TestCase):

    def test_base_case(self):
        solution = PascalsTriangle()

        expected_result = [[1]]
        triangle_rows = solution.generate(1)

        self.assertEqual(expected_result, triangle_rows)

    def test_default_input(self):
        solution = PascalsTriangle()

        expected_result = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        triangle_rows = solution.generate(5)

        self.assertEqual(expected_result, triangle_rows)
