from unittest import TestCase

from .kth_largest_element_in_an_array import KthLargestElementInAnArray


class KthLargestElementInAnArrayTest(TestCase):

    def test_default_input(self):
        solution = KthLargestElementInAnArray()

        self.assertEqual(5, solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))
        self.assertEqual(4, solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
