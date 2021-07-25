from unittest import TestCase

from binary_search import BinarySearch


class BinarySearchTest(TestCase):
    def test_existing_input(self):
        solution = BinarySearch()

        self.assertEqual(
            4,
            solution.search([-1, 0, 3, 5, 9, 12], 9)
        )

        self.assertEqual(
            0,
            solution.search([5], 5)
        )

        self.assertEqual(
            1,
            solution.search([2, 5], 5)
        )

    def test_notfound_input(self):
        solution = BinarySearch()

        self.assertEqual(
            -1,
            solution.search([-1, 0, 3, 5, 9, 12], 2)
        )