from typing import List
from unittest import TestCase

from word_break import WordBreak


class WordBreakTest(TestCase):
    def test_can_segment(self):
        solution = WordBreak()

        self.assertTrue(solution.wordBreak('leetcode', ['leet', 'code']))
        self.assertTrue(solution.wordBreak('applepenapple', ['apple', 'pen']))

    def test_canot_segment(self):
        solution = WordBreak()

        self.assertFalse(solution.wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']))
