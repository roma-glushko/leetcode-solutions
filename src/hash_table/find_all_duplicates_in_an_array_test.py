from unittest import TestCase

from .find_all_duplicates_in_an_array import FindAllDuplicatedInAnArray


class FindAllDuplicatedInAnArrayTest(TestCase):
    def test_base_input(self):
        solution = FindAllDuplicatedInAnArray()

        self.assertCountEqual([2, 3], solution.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))

        self.assertCountEqual([1], solution.findDuplicates([1, 1, 2]))

    def test_no_duplicates_input(self):
        solution = FindAllDuplicatedInAnArray()

        self.assertCountEqual([], solution.findDuplicates([1]))
