from itertools import accumulate
from typing import List


class JumpGameII:
    """
    Problem Link: https://leetcode.com/problems/jump-game-ii/
    Complexity: Medium
    Runtime: 124 ms
    Memory: 15.4 MB
    """
    def jump(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len <= 1:
            # already at the final cell
            return 0

        last_cell_idx: int = nums_len - 1
        farthest_cell_idx_at = [*accumulate([idx + jump_offset for idx, jump_offset in enumerate(nums)], max)]

        # let's jump as far as we can

        current_cell_idx: int = 0
        num_jumps = 0

        while current_cell_idx < last_cell_idx:
            current_cell_idx = farthest_cell_idx_at[current_cell_idx]
            num_jumps += 1

        return num_jumps
