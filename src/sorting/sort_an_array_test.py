from unittest import TestCase

from .sort_an_array import SortAnArray


class SortAnArrayTest(TestCase):

    def test_default_input(self):
        solution = SortAnArray()

        self.assertEqual(solution.sortArray([5, 2, 3, 1]), [1, 2, 3, 5])
        self.assertEqual(solution.sortArray([5, 1, 1, 2, 0, 0]), [0, 0, 1, 1, 2, 5])

    def test_sorted_array(self):
        solution = SortAnArray()

        self.assertEqual(solution.sortArray([0, 0, 1, 1, 2, 5]), [0, 0, 1, 1, 2, 5])

    def test_same_elements_array(self):
        solution = SortAnArray()

        self.assertEqual(solution.sortArray([7, 7, 7, 7, 7, 7]), [7, 7, 7, 7, 7, 7])
