from typing import List


class CountingBits:
    """
    Problem Link: https://leetcode.com/problems/counting-bits/
    Complexity: Easy
    """

    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        bits_number: List[int] = [0, 1]

        if n == 1:
            return bits_number

        next_two_power: int = 2
        count_index: int = 0

        for number in range(2, n + 1):
            if number == next_two_power:
                # we should reset count index at each number that is power of 2
                next_two_power *= 2
                count_index = 0

            bits_number.append(1 + bits_number[count_index])
            count_index += 1

        return bits_number
