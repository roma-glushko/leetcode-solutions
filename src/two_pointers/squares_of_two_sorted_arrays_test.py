from unittest import TestCase

from .squares_of_two_sorted_arrays import SquaresOfTwoSortedArrays


class SquaresOfTwoSortedArraysTest(TestCase):

    def test_input1(self):
        solution = SquaresOfTwoSortedArrays()

        self.assertEqual(
            [0, 1, 9, 16, 100],
            solution.sortedSquares([-4, -1, 0, 3, 10])
        )

    def test_input2(self):
        solution = SquaresOfTwoSortedArrays()

        self.assertEqual(solution.sortedSquares([-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121])

    def test_only_negatives(self):
        solution = SquaresOfTwoSortedArrays()

        self.assertEqual(solution.sortedSquares([-10, -7, -3, -2, -1]), [1, 4, 9, 49, 100])

    def test_most_negatives(self):
        solution = SquaresOfTwoSortedArrays()

        self.assertEqual(solution.sortedSquares([-10, -7, -3, -2, -1, 0, 4]), [0, 1, 4, 9, 16, 49, 100])
