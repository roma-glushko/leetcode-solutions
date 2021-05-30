from unittest import TestCase

from .reverse_integer import ReverseInteger


class TestReverseInteger(TestCase):

    def test_default_grid(self):
        solution = ReverseInteger()
        perimeter = solution.reverse(123)

        self.assertEqual(perimeter, 321)
