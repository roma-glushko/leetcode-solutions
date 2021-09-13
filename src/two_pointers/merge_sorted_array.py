from typing import List


class MergeSortedArray:
    """
    Problem Link: https://leetcode.com/problems/merge-sorted-array/
    Complexity: Easy
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, full_array_size = m - 1, n - 1, n + m - 1

        for idx in range(full_array_size, -1, -1):
            if j < 0:
                break

            if i >= 0 and nums1[i] > nums2[j]:
                nums1[idx] = nums1[i]
                i -= 1
                continue

            # try to finalize the second array faster
            nums1[idx] = nums2[j]
            j -= 1
