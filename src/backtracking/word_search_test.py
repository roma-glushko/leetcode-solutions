from unittest import TestCase

from .word_search import WordSearch


class WordSearchTest(TestCase):
    def test_default_function(self):
        solution = WordSearch()

        char_matrix = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ]

        self.assertTrue(
            solution.exist(
                char_matrix,
                "ABCCED",
            )
        )

        self.assertTrue(
            solution.exist(
                char_matrix,
                "SEE",
            )
        )

        self.assertFalse(
            solution.exist(
                char_matrix,
                "ABCB",
            )
        )
