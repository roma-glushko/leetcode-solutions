from typing import List


class BinarySearch:
    """
    Problem Link: https://leetcode.com/problems/binary-search/
    Complexity: Easy

    Runtime: 232ms
    Memory: 15.6MB
    """

    def search(self, nums: List[int], target: int) -> int:
        left_idx: int = 0
        right_idx: int = len(nums) - 1

        while left_idx < right_idx:
            middle_idx = (left_idx + right_idx) // 2

            if nums[middle_idx] == target:
                return middle_idx

            if nums[middle_idx] > target:
                right_idx = middle_idx - 1

            if nums[middle_idx] < target:
                left_idx = middle_idx + 1

        if nums[left_idx] == target:
            return left_idx

        return -1
