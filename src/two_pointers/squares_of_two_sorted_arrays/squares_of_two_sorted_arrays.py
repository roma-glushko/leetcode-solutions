from typing import List


class SquaresOfTwoSortedArrays:
    """
    Problem Link: https://leetcode.com/problems/squares-of-a-sorted-array/
    Complexity: Easy
    """

    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1

        idx = j
        squares = [0] * len(nums)

        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                squares[idx] = nums[i] ** 2
                i += 1
            else:
                squares[idx] = nums[j] ** 2
                j -= 1

            idx -= 1

        return squares
