from unittest import TestCase

from .reverse_string import ReverseString


class ReverseStringTest(TestCase):

    def test_default_input(self):
        solution = ReverseString()

        result_array = ["h", "e", "l", "l", "o"]
        solution.reverse_string(result_array)

        self.assertEqual(result_array, ["o", "l", "l", "e", "h"])