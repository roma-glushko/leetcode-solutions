from .longest_consecutive_sequence import LongestConsecutiveSequence


def test_four_input():
    solution = LongestConsecutiveSequence()
    assert 4 == solution.longestConsecutive([100, 4, 200, 1, 3, 2])
    assert 4 == solution.longestConsecutive2([100, 4, 200, 1, 3, 2])


def test_nine_input():
    solution = LongestConsecutiveSequence()
    assert 9 == solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
    assert 9 == solution.longestConsecutive2([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])


def test_consequent_input():
    solution = LongestConsecutiveSequence()
    assert 6 == solution.longestConsecutive([0, 1, 2, 3, 4, 5])
    assert 6 == solution.longestConsecutive2([0, 1, 2, 3, 4, 5])


def test_nonconsequent_input():
    solution = LongestConsecutiveSequence()
    assert 1 == solution.longestConsecutive([0, 2, 4, 6, 100, 200, 500])
    assert 1 == solution.longestConsecutive2([0, 2, 4, 6, 100, 200, 500])


def test_single_num_input():
    solution = LongestConsecutiveSequence()
    assert 1 == solution.longestConsecutive([500])
    assert 1 == solution.longestConsecutive2([500])
