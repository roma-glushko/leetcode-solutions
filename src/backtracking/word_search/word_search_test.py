from .word_search import WordSearch


def test_default_function():
    solution = WordSearch()
    char_matrix = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert solution.exist(char_matrix, "ABCCED")
    assert solution.exist(char_matrix, "SEE")
    assert not solution.exist(char_matrix, "ABCB")
