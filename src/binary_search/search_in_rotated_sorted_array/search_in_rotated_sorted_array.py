from typing import List


class SearchInRotatedSortedArray:
    """
    Problem Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
    Complexity: Medium
    """

    def search(self, nums: List[int], target: int) -> int:
        start_idx = 0
        end_idx = len(nums) - 1

        while start_idx < end_idx:
            middle_idx: int = (end_idx + start_idx) // 2

            if nums[middle_idx] == target:
                return middle_idx

            if nums[start_idx] <= nums[middle_idx]:
                # left subarray is still sorted after rotation

                if nums[start_idx] <= target <= nums[middle_idx]:
                    end_idx = middle_idx
                else:
                    start_idx = middle_idx + 1

                continue

            # right subarray is still sorted after rotation

            if nums[middle_idx] <= target <= nums[end_idx]:
                start_idx = middle_idx + 1
            else:
                end_idx = middle_idx

        if nums[end_idx] == target:
            return end_idx

        if nums[start_idx] == target:
            return start_idx

        return -1
