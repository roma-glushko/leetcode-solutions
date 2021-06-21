from unittest import TestCase

from .longest_common_subsequence import LongestCommonSubsequence


class LongestCommonSubsequenceTest(TestCase):

    def test_four_input(self):
        solution = LongestCommonSubsequence()

        self.assertEqual(solution.longestCommonSubsequence('abcde', 'ace'), 3)  # LCS: ace

    def test_same_strings(self):
        solution = LongestCommonSubsequence()

        self.assertEqual(solution.longestCommonSubsequence('abc', 'abc'), 3)  # LCS: abc

    def test_no_lcs(self):
        solution = LongestCommonSubsequence()

        self.assertEqual(solution.longestCommonSubsequence('abc', 'def'), 0)

    def test_one_lcs(self):
        solution = LongestCommonSubsequence()

        self.assertEqual(solution.longestCommonSubsequence('a', 'defgab'), 1)  # LCS: a

    def test_one_common_in_longer_strings(self):
        solution = LongestCommonSubsequence()

        self.assertEqual(solution.longestCommonSubsequence('bsbininm', 'jmjkbkjkv'), 1)  # LCS: b

    def test_duplicated_chars(self):
        solution = LongestCommonSubsequence()

        self.assertEqual(solution.longestCommonSubsequence('zxvvyzw', 'xkykzpw'), 4)  # LCS: xyzw
