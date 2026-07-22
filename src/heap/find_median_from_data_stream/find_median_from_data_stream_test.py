import pytest
from .find_median_from_data_stream import FindMedianFromDataStream


def test_default_input():
    solution = FindMedianFromDataStream()
    solution.addNum(1)
    solution.addNum(2)
    assert solution.findMedian() == pytest.approx(1.5)
    solution.addNum(3)
    assert solution.findMedian() == pytest.approx(2)
    solution.addNum(4)
    assert solution.findMedian() == pytest.approx(2.5)
    solution.addNum(5)
    assert solution.findMedian() == pytest.approx(3)
    solution.addNum(-1)
    assert solution.findMedian() == pytest.approx(2.5)
