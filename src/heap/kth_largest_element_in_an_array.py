from typing import List
from heapq import heappush, heappushpop


class KthLargestElementInAnArray:
    """
    Problem Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
    Complexity: Medium
    Runtime: 64ms
    Memory: 15MB
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_largest_elements: List[int] = []

        for element in nums:
            if len(k_largest_elements) < k:
                heappush(k_largest_elements, element)
                continue

            if element < k_largest_elements[0]:
                # element is too small to replace the smallest element among kth largest ones
                continue

            # largest_elements heap is full, needs to pop the smallest item from it
            heappushpop(k_largest_elements, element)

        return k_largest_elements[0]


