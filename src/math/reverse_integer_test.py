from unittest import TestCase

from .reverse_integer import ReverseInteger


class ReverseIntegerTest(TestCase):

    def test_default_input(self):
        solution = ReverseInteger()
        reversed_number = solution.reverse(123)

        self.assertEqual(reversed_number, 321)
