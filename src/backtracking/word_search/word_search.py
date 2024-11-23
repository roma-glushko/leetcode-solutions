from typing import List, Set


class WordSearch:
    """
    Problem Link: https://leetcode.com/problems/word-search/
    Complexity: Medium
    Runtime: 6300ms
    Memory: 14.5MB
    """

    def track_word(
        self,
        board: List[List[str]],
        row_idx: int,
        column_idx: int,
        word: str,
        visited_cells: Set,
    ) -> bool:
        if f"{row_idx}:{column_idx}" in visited_cells:
            return False

        if len(word) == 0:
            return True

        visited_cells.add(f"{row_idx}:{column_idx}")

        row_nums: int = len(board)
        column_nums: int = len(board[0])
        word_was_found: bool = False

        if column_idx + 1 < column_nums and board[row_idx][column_idx + 1] == word[0]:
            word_was_found = word_was_found or self.track_word(
                board, row_idx, column_idx + 1, word[1:], visited_cells
            )

        if row_idx + 1 < row_nums and board[row_idx + 1][column_idx] == word[0]:
            word_was_found = word_was_found or self.track_word(
                board, row_idx + 1, column_idx, word[1:], visited_cells
            )

        if row_idx - 1 >= 0 and board[row_idx - 1][column_idx] == word[0]:
            word_was_found = word_was_found or self.track_word(
                board, row_idx - 1, column_idx, word[1:], visited_cells
            )

        if column_idx - 1 >= 0 and board[row_idx][column_idx - 1] == word[0]:
            word_was_found = word_was_found or self.track_word(
                board, row_idx, column_idx - 1, word[1:], visited_cells
            )

        visited_cells.remove(f"{row_idx}:{column_idx}")

        return word_was_found

    def exist(self, board: List[List[str]], word: str) -> bool:
        row_nums: int = len(board)
        column_nums: int = len(board[0])
        visited_cells: Set = set()

        for i in range(row_nums):
            for j in range(column_nums):
                if board[i][j] != word[0]:
                    continue

                if not self.track_word(board, i, j, word[1:], visited_cells):
                    continue

                return True

        return False
