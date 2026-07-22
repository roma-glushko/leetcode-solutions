from .binary_search import BinarySearch


def test_existing_input():
    solution = BinarySearch()
    assert 4 == solution.search([-1, 0, 3, 5, 9, 12], 9)
    assert 0 == solution.search([5], 5)
    assert 1 == solution.search([2, 5], 5)


def test_notfound_input():
    solution = BinarySearch()
    assert -1 == solution.search([-1, 0, 3, 5, 9, 12], 2)
