class FindAllDuplicatedInAnArray:
    """
    Problem Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/
    Complexity: Medium

    Runtime: 316ms
    Memory: 23.4MB
    """

    def findDuplicates(self, nums: list[int]) -> list[int]:
        detected_numbers: set = set()
        duplicated_numbers: list[int] = []

        for number in nums:
            if number in detected_numbers:
                duplicated_numbers.append(number)
                continue

            detected_numbers.add(number)

        return duplicated_numbers
