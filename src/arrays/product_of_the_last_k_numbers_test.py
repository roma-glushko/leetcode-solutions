from unittest import TestCase

from .product_of_the_last_k_numbers import ProductOfTheLastKNumbers


class ProductOfTheLastKNumbersTest(TestCase):

    def test_base_case(self):
        solution = ProductOfTheLastKNumbers()

        for num in [3, 0, 2, 5, 4]:
            solution.add(num)

        self.assertEqual(20, solution.getProduct(2))
        self.assertEqual(40, solution.getProduct(3))
        self.assertEqual(0, solution.getProduct(4))

        solution.add(8)
        self.assertEqual(32, solution.getProduct(2))
        self.assertEqual(0, solution.getProduct(10))

    def test_one_numbers_case(self):
        solution = ProductOfTheLastKNumbers()

        for num in [2, 4, 1, 7, 4, 1, 4, 2]:
            solution.add(num)

        self.assertEqual(8, solution.getProduct(3))
        self.assertEqual(224, solution.getProduct(5))
        self.assertEqual(224, solution.getProduct(6))
        self.assertEqual(1792, solution.getProduct(8))

        solution.add(4)

    def test_long_sequence_case(self):
        solution = ProductOfTheLastKNumbers()

        for num in [1] * 100_000:
            solution.add(num)

        self.assertEqual(1, solution.getProduct(100_000))
