from unittest import TestCase

from .counting_bits import CountingBits


class CountingBitsTest(TestCase):
    def test_default_inputs(self):
        solution = CountingBits()

        bit_array = solution.countBits(2)
        self.assertEqual(bit_array, [0, 1, 1])

        bit_array = solution.countBits(3)
        self.assertEqual(bit_array, [0, 1, 1, 2])

        bit_array = solution.countBits(4)
        self.assertEqual(bit_array, [0, 1, 1, 2, 1])

        bit_array = solution.countBits(5)
        self.assertEqual(bit_array, [0, 1, 1, 2, 1, 2])

    def test_base_cases(self):
        solution = CountingBits()

        bit_array = solution.countBits(0)
        self.assertEqual(bit_array, [0])

        bit_array = solution.countBits(1)
        self.assertEqual(bit_array, [0, 1])
