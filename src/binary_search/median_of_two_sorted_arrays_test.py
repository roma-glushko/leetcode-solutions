from unittest import TestCase

from .median_of_two_sorted_arrays import MedianOfTwoSortedArrays


class MedianOfTwoSortedArraysTest(TestCase):
    def test_default_input(self):
        solution = MedianOfTwoSortedArrays()

        self.assertAlmostEqual(
            11,
            solution.findMedianSortedArrays(
                [1, 3, 8, 9, 15],
                [7, 11, 18, 19, 21, 25],
            ),
        )

        self.assertAlmostEqual(
            2.0,
            solution.findMedianSortedArrays(
                [1, 3],
                [2],
            ),
        )

        self.assertAlmostEqual(
            2.5,
            solution.findMedianSortedArrays(
                [1, 2],
                [3, 4],
            ),
        )

    def test_zero_arrays(self):
        solution = MedianOfTwoSortedArrays()

        self.assertAlmostEqual(
            0.0,
            solution.findMedianSortedArrays(
                [0, 0],
                [0, 0],
            ),
        )

    def test_empty_arrays(self):
        solution = MedianOfTwoSortedArrays()

        self.assertAlmostEqual(
            1.0,
            solution.findMedianSortedArrays(
                [],
                [1],
            ),
        )

        self.assertAlmostEqual(
            2.0,
            solution.findMedianSortedArrays(
                [2],
                [],
            ),
        )

        self.assertAlmostEqual(
            1.5,
            solution.findMedianSortedArrays(
                [1, 2],
                [],
            ),
        )

        self.assertAlmostEqual(
            2,
            solution.findMedianSortedArrays(
                [],
                [1, 2, 3],
            ),
        )

    def test_negative_numbers(self):
        solution = MedianOfTwoSortedArrays()

        self.assertAlmostEqual(
            -1,
            solution.findMedianSortedArrays(
                [3],
                [-2, -1],
            ),
        )
