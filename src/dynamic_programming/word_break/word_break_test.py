from .word_break import WordBreak


def test_can_segment():
    solution = WordBreak()
    assert solution.wordBreak("leetcode", ["leet", "code"])
    assert solution.wordBreak("applepenapple", ["apple", "pen"])


def test_canot_segment():
    solution = WordBreak()
    assert not solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
