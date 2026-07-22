from .longest_common_subsequence import LongestCommonSubsequence


def test_four_input():
    solution = LongestCommonSubsequence()
    assert solution.longestCommonSubsequence("abcde", "ace") == 3


def test_same_strings():
    solution = LongestCommonSubsequence()
    assert solution.longestCommonSubsequence("abc", "abc") == 3


def test_no_lcs():
    solution = LongestCommonSubsequence()
    assert solution.longestCommonSubsequence("abc", "def") == 0


def test_one_lcs():
    solution = LongestCommonSubsequence()
    assert solution.longestCommonSubsequence("a", "defgab") == 1


def test_one_common_in_longer_strings():
    solution = LongestCommonSubsequence()
    assert solution.longestCommonSubsequence("bsbininm", "jmjkbkjkv") == 1


def test_duplicated_chars():
    solution = LongestCommonSubsequence()
    assert solution.longestCommonSubsequence("zxvvyzw", "xkykzpw") == 4
