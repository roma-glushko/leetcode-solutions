class ReverseInteger:
    """
    Problem Link: https://leetcode.com/problems/reverse-integer/
    Complexity: Easy
    """
    def reverse(self, x: int) -> int:
        resersed_x = 0

        while x != 0:
            reminder = x % 10
            x = x // 10

            resersed_x = resersed_x * 10 + reminder

        if (resersed_x >= 2 ** 31 - 1) or (resersed_x <= -2 ** 31):
            return 0

        return resersed_x