from .search_in_rotated_sorted_array import SearchInRotatedSortedArray


def test_default_input():
    solution = SearchInRotatedSortedArray()
    assert 4 == solution.search([4, 5, 6, 7, 0, 1, 2], 0)


def test_not_found_elements():
    solution = SearchInRotatedSortedArray()
    assert -1 == solution.search([4, 5, 6, 7, 0, 1, 2], 3)
    assert -1 == solution.search([1], 0)


def test_single_element_array():
    solution = SearchInRotatedSortedArray()
    assert 0 == solution.search([1], 1)


def test_border_elements():
    solution = SearchInRotatedSortedArray()
    assert 2 == solution.search([5, 1, 3], 3)
    assert 0 == solution.search([5, 1, 3], 5)
