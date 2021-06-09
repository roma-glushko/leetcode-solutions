from typing import List


class TwoSum:
    """
    Problem Link: https://leetcode.com/problems/two-sum/
    Complexity: Easy
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        available_numbers = {num: idx for idx, num in enumerate(nums)}

        for idx, num in enumerate(nums):
            remaining_number = target - num

            if remaining_number in available_numbers and available_numbers[remaining_number] != idx:
                remaining_idx = available_numbers[remaining_number]

                return idx, remaining_idx

        return ()