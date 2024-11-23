from typing import List


class LongestCommonSubsequence:
    """
    Problem Link: https://leetcode.com/problems/longest-common-subsequence/
    Complexity: Medium
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1_len: int = len(text1)
        text2_len: int = len(text2)

        longest_subseq_lengths: List[List[int]] = [
            [0] * (text2_len + 1) for _ in range(text1_len + 1)
        ]

        for i in range(1, text1_len + 1):
            for j in range(1, text2_len + 1):
                # the current longest subseq len consists of
                # the longest subseq len from the shorter sequences
                current_longest_subseq_len: int = max(
                    longest_subseq_lengths[i - 1][j], longest_subseq_lengths[i][j - 1]
                )

                if text1[i - 1] == text2[j - 1]:
                    # found a new char match, should increase the longest subseq len at this point
                    current_longest_subseq_len = (
                        1 + longest_subseq_lengths[i - 1][j - 1]
                    )

                longest_subseq_lengths[i][j] = current_longest_subseq_len

        return longest_subseq_lengths[-1][
            -1
        ]  # the very last cell will have the longest possible length
