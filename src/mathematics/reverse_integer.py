class ReverseInteger:
    """
    Problem Link: https://leetcode.com/problems/reverse-integer/
    Complexity: Easy
    """

    def reverse(self, x: int) -> int:
        reversed_x = 0

        while x != 0:
            reminder = x % 10
            x = x // 10

            reversed_x = reversed_x * 10 + reminder

        if (reversed_x >= 2**31 - 1) or (reversed_x <= -(2**31)):
            return 0

        return reversed_x
