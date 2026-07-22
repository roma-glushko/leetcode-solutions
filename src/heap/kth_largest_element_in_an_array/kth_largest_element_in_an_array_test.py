from .kth_largest_element_in_an_array import KthLargestElementInAnArray


def test_default_input():
    solution = KthLargestElementInAnArray()
    assert 5 == solution.findKthLargest([3, 2, 1, 5, 6, 4], 2)
    assert 4 == solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
