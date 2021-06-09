from typing import List


class ReverseString:
    """
    Problem Link: https://leetcode.com/problems/reverse-string/
    Complexity: Easy
    """
    def reverse_string(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1

        while i < j:
            s[i], s[j] = s[j], s[i]

            i += 1
            j -= 1
