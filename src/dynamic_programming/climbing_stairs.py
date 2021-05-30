class ClimbingStairs:
    """
    Problem Link: https://leetcode.com/problems/climbing-stairs/
    """
    def climbStairs(self, n: int) -> int:
        steps = [0, 1, 2]

        for i in range(3, n + 1):
            steps.append(steps[i - 1] + steps[i - 2])

        return steps[n]