from unittest import TestCase

from .merge_sorted_array import MergeSortedArray


class MergeSortedArrayTest(TestCase):

    def test_two_arrays(self):
        solution = MergeSortedArray()

        result_array = [1, 2, 3, 0, 0, 0]
        solution.merge(result_array, 3, [2, 5, 6], 3)

        self.assertEqual(result_array, [1, 2, 2, 3, 5, 6])

    def test_one_array_empty(self):
        solution = MergeSortedArray()

        result_array = [1]
        solution.merge(result_array, 1, [], 0)

        self.assertEqual(result_array, [1])

    def test_second_array_empty(self):
        solution = MergeSortedArray()

        result_array = [0]
        solution.merge(result_array, 0, [1], 1)

        self.assertEqual(result_array, [1])