from unittest import TestCase

from .search_in_rotated_sorted_array import SearchInRotatedSortedArray


class SearchInRotatedSortedArrayTest(TestCase):
    def test_default_input(self):
        solution = SearchInRotatedSortedArray()

        self.assertEqual(4, solution.search([4, 5, 6, 7, 0, 1, 2], 0))

    def test_not_found_elements(self):
        solution = SearchInRotatedSortedArray()

        self.assertEqual(-1, solution.search([4, 5, 6, 7, 0, 1, 2], 3))
        self.assertEqual(-1, solution.search([1], 0))

    def test_single_element_array(self):
        solution = SearchInRotatedSortedArray()

        self.assertEqual(0, solution.search([1], 1))

    def test_border_elements(self):
        solution = SearchInRotatedSortedArray()

        self.assertEqual(2, solution.search([5, 1, 3], 3))
        self.assertEqual(0, solution.search([5, 1, 3], 5))
