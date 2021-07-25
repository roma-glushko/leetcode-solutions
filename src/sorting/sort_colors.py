from typing import List


class SortColors:
    """
    Problem Link: https://leetcode.com/problems/sort-colors/
    Complexity: Medium

    Runtime: 32ms
    Memory: 14.4MB
    """
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors: List[int] = [0, 0, 0]

        for color_idx in nums:
            colors[color_idx] += 1

        nums.clear()

        for color_idx in range(0, len(colors)):
            if colors[color_idx] <= 0:
                continue

            nums.extend([color_idx] * colors[color_idx])