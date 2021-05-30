from unittest import TestCase

from .climbing_stairs import ClimbingStairs


class ClimbingStairsTest(TestCase):

    def test_two_stairs(self):
        solution = ClimbingStairs()
        num_of_ways = solution.climbStairs(2)

        self.assertEqual(num_of_ways, 2)

    def test_three_stairs(self):
        solution = ClimbingStairs()
        num_of_ways = solution.climbStairs(3)

        self.assertEqual(num_of_ways, 3)
