from .sort_an_array import SortAnArray


def test_default_input():
    solution = SortAnArray()
    assert solution.sortArray([5, 2, 3, 1]) == [1, 2, 3, 5]
    assert solution.sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]


def test_sorted_array():
    solution = SortAnArray()
    assert solution.sortArray([0, 0, 1, 1, 2, 5]) == [0, 0, 1, 1, 2, 5]


def test_same_elements_array():
    solution = SortAnArray()
    assert solution.sortArray([7, 7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7, 7]
