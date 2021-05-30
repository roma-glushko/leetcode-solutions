from unittest import TestCase

from .climbing_stairs import ClimbingStairs


class TestBestTimeToBuyAndSellStock(TestCase):

    def test_two_stairs(self):
        solution = ClimbingStairs()
        perimeter = solution.climbStairs(2)

        self.assertEqual(perimeter, 2)

    def test_three_stairs(self):
        solution = ClimbingStairs()
        perimeter = solution.climbStairs(3)

        self.assertEqual(perimeter, 3)
