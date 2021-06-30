import math
from typing import List


class MedianOfTwoSortedArrays:
    """
    Problem Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
    Complexity: Hard

    Runtime: 96ms
    Memory: 14.6MB
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_size: int = len(nums1) + len(nums2)
        total_half_size: int = (total_size + 1) // 2  #

        def get_median_from_centers(
                num1_max_left_elem: int,
                num2_max_left_elem: int,
                num1_min_right_elem: int,
                num2_min_right_elem: int
        ) -> float:
            if total_size % 2 != 0:
                return max(num1_max_left_elem, num2_max_left_elem)

            return 0.5 * (
                    max(num1_max_left_elem, num2_max_left_elem) +
                    min(num1_min_right_elem, num2_min_right_elem)
            )

        def get_median_from_array(numbers: List[int]) -> float:
            if total_size % 2 != 0:
                return numbers[total_half_size - 1]  # middle element idx = total_half_size - 1

            return 0.5 * (numbers[total_half_size - 1] + numbers[total_half_size])

        if len(nums1) == 0 or len(nums2) == 0:
            return get_median_from_array(nums1 if len(nums1) != 0 else nums2)

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        left_num1_idx, right_num1_idx = 0, len(nums1) - 1

        while left_num1_idx <= right_num1_idx:
            middle_num1_idx: int = (right_num1_idx + left_num1_idx) // 2
            left_num2_idx: int = total_half_size - middle_num1_idx - 2

            num1_max_left_elem: int = nums1[middle_num1_idx] if middle_num1_idx >= 0 else -math.inf
            num1_min_right_elem: int = nums1[middle_num1_idx + 1] if middle_num1_idx + 1 < len(nums1) else math.inf

            num2_max_left_elem: int = nums2[left_num2_idx] if left_num2_idx >= 0 else -math.inf
            num2_min_right_elem: int = nums2[left_num2_idx + 1] if left_num2_idx + 1 < len(nums2) else math.inf

            if num1_max_left_elem <= num2_min_right_elem and num2_max_left_elem <= num1_min_right_elem:
                return get_median_from_centers(
                    num1_max_left_elem,
                    num2_max_left_elem,
                    num1_min_right_elem,
                    num2_min_right_elem,
                )

            if num1_max_left_elem > num2_min_right_elem:
                right_num1_idx = middle_num1_idx - 1

            if num1_max_left_elem <= num2_min_right_elem:
                left_num1_idx = middle_num1_idx + 1

        # when loop above is complete without success, we need to apply the same logic to the final indices
        # as they may be negative indicating that one of the arrays has no items on the left side like:
        # [3], [-2, -1]

        middle_num1_idx: int = (right_num1_idx + left_num1_idx) // 2
        left_num2_idx: int = total_half_size - middle_num1_idx - 2

        num1_max_left_elem: int = nums1[middle_num1_idx] if middle_num1_idx >= 0 else -math.inf
        num1_min_right_elem: int = nums1[middle_num1_idx + 1] if middle_num1_idx + 1 < len(nums1) else math.inf

        num2_max_left_elem: int = nums2[left_num2_idx] if left_num2_idx >= 0 else -math.inf
        num2_min_right_elem: int = nums2[left_num2_idx + 1] if left_num2_idx + 1 < len(nums2) else math.inf

        return get_median_from_centers(
            num1_max_left_elem,
            num2_max_left_elem,
            num1_min_right_elem,
            num2_min_right_elem,
        )