from collections import defaultdict
from typing import List, Dict


class LongestConsecutiveSequence:
    """
    Problem Link: https://leetcode.com/problems/longest-consecutive-sequence/
    Complexity: Medium
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        This solution is based on idea that steak for the current number num = 1 + steak(num - 1)
        """
        available_nums = set(nums)
        sequences_len_map: Dict[int, int] = defaultdict(int)
        max_steak: int = 0

        def get_steak_at(num: int) -> int:
            """
            Retrieve steaks for shorter sequences
            """
            if num not in available_nums:
                return 0

            if num in sequences_len_map:
                # add the current steak to the max streak we could reach from prev_consecutive_num
                # it's going to be at least bigger by one
                return sequences_len_map[num]

            # needs to calculate the steak
            steak = 1 + get_steak_at(num - 1)
            sequences_len_map[num] = steak

            return steak

        for num in nums:
            if num in sequences_len_map:
                max_steak = max(max_steak, sequences_len_map[num])
                continue

            current_steak: int = 1 + get_steak_at(num - 1)

            # saves the max steak we could reach from num
            sequences_len_map[num] = current_steak
            max_steak = max(current_steak, max_steak)

        return max_steak

    def longestConsecutive2(self, nums: List[int]) -> int:
        """
        This solution is based on idea of finding the beginnings of the sequences and iterate from there until the end.
        Each possible sequence would be checked once.
        """
        available_nums = set(nums)
        max_peak: int = 0

        for num in nums:
            if num - 1 in available_nums:
                continue

            # found a beginning of the sequence
            end_num: int = num + 1

            while end_num in available_nums:
                # iterate until the end
                end_num += 1

            max_peak = max(max_peak, end_num - num)

        return max_peak