from unittest import TestCase

from .longest_consecutive_sequence import LongestConsecutiveSequence


class LongestConsecutiveSequenceTest(TestCase):

    def test_four_input(self):
        solution = LongestConsecutiveSequence()

        self.assertEqual(
            4,
            solution.longestConsecutive([100, 4, 200, 1, 3, 2]),
        )

        self.assertEqual(
            4,
            solution.longestConsecutive2([100, 4, 200, 1, 3, 2]),
        )

    def test_nine_input(self):
        solution = LongestConsecutiveSequence()

        self.assertEqual(
            9,
            solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]),
        )

        self.assertEqual(
            9,
            solution.longestConsecutive2([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]),
        )

    def test_consequent_input(self):
        solution = LongestConsecutiveSequence()

        self.assertEqual(
            6,
            solution.longestConsecutive([0, 1, 2, 3, 4, 5]),
        )

        self.assertEqual(
            6,
            solution.longestConsecutive2([0, 1, 2, 3, 4, 5]),
        )

    def test_nonconsequent_input(self):
        solution = LongestConsecutiveSequence()

        self.assertEqual(
            1,
            solution.longestConsecutive([0, 2, 4, 6, 100, 200, 500]),
        )

        self.assertEqual(
            1,
            solution.longestConsecutive2([0, 2, 4, 6, 100, 200, 500]),
        )

    def test_single_num_input(self):
        solution = LongestConsecutiveSequence()

        self.assertEqual(
            1,
            solution.longestConsecutive([500]),
        )

        self.assertEqual(
            1,
            solution.longestConsecutive2([500]),
        )