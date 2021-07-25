from typing import List, Set


class FindAllDuplicatedInAnArray:
    """
    Problem Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/
    Complexity: Medium

    Runtime: 316ms
    Memory: 23.4MB
    """
    def findDuplicates(self, nums: List[int]) -> List[int]:
        detected_numbers: Set = set()
        duplicated_numbers: List[int] = []

        for number in nums:
            if number in detected_numbers:
                duplicated_numbers.append(number)
                continue

            detected_numbers.add(number)

        return duplicated_numbers