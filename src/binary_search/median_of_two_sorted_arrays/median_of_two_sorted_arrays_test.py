import pytest
from .median_of_two_sorted_arrays import MedianOfTwoSortedArrays


def test_default_input():
    solution = MedianOfTwoSortedArrays()
    assert solution.findMedianSortedArrays(
        [1, 3, 8, 9, 15], [7, 11, 18, 19, 21, 25]
    ) == pytest.approx(11)
    assert solution.findMedianSortedArrays([1, 3], [2]) == pytest.approx(2.0)
    assert solution.findMedianSortedArrays([1, 2], [3, 4]) == pytest.approx(2.5)


def test_zero_arrays():
    solution = MedianOfTwoSortedArrays()
    assert solution.findMedianSortedArrays([0, 0], [0, 0]) == pytest.approx(0.0)


def test_empty_arrays():
    solution = MedianOfTwoSortedArrays()
    assert solution.findMedianSortedArrays([], [1]) == pytest.approx(1.0)
    assert solution.findMedianSortedArrays([2], []) == pytest.approx(2.0)
    assert solution.findMedianSortedArrays([1, 2], []) == pytest.approx(1.5)
    assert solution.findMedianSortedArrays([], [1, 2, 3]) == pytest.approx(2)


def test_negative_numbers():
    solution = MedianOfTwoSortedArrays()
    assert solution.findMedianSortedArrays([3], [-2, -1]) == pytest.approx(-1)
