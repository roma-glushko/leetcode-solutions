from .climbing_stairs import ClimbingStairs


def test_two_stairs():
    solution = ClimbingStairs()
    num_of_ways = solution.climbStairs(2)
    assert num_of_ways == 2


def test_three_stairs():
    solution = ClimbingStairs()
    num_of_ways = solution.climbStairs(3)
    assert num_of_ways == 3
