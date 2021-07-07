from collections import Counter
from typing import List, Set


class ThreeSum:
    """
    Problem Link: https://leetcode.com/problems/3sum/
    Complexity: Medium

    Runtime: 3352ms
    Memory: 17MB
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_len: int = len(nums)
        if num_len == 0:
            return []

        nums = sorted(nums)
        triplets = set()

        for first_num_idx, first_num in enumerate(nums):
            range_left_idx = first_num_idx + 1
            range_right_idx = num_len - 1

            target = -first_num

            while range_left_idx < range_right_idx:
                second_num: int = nums[range_left_idx]
                third_num: int = nums[range_right_idx]

                if second_num + third_num == target:
                    triplets.add((first_num, second_num, third_num))

                if second_num + third_num > target:
                    range_right_idx -= 1

                if second_num + third_num <= target:
                    range_left_idx += 1

        return list(triplets)