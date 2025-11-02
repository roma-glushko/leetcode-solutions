from unittest import TestCase
import pytest
from .find_median_from_data_stream import FindMedianFromDataStream, FindMedianFromDataStreamV2


class FindMedianFromDataStreamTest(TestCase):
    def test_default_input(self):
        solution = FindMedianFromDataStream()

        solution.addNum(1)
        solution.addNum(2)
        self.assertAlmostEqual(1.5, solution.findMedian())

        solution.addNum(3)
        self.assertAlmostEqual(2, solution.findMedian())

        solution.addNum(4)
        self.assertAlmostEqual(2.5, solution.findMedian())

        solution.addNum(5)
        self.assertAlmostEqual(3, solution.findMedian())

        solution.addNum(-1)
        self.assertAlmostEqual(2.5, solution.findMedian())


def test__find_median_from_data_stream_v2():
    solution = FindMedianFromDataStreamV2()

    solution.addNum(1)
    solution.addNum(2)

    assert pytest.approx(1.5) == solution.findMedian()

    solution.addNum(3)
    assert 2 == solution.findMedian()

    solution.addNum(4)
    assert pytest.approx(2.5) == solution.findMedian()

    solution.addNum(5)
    assert pytest.approx(3) == solution.findMedian()

    solution.addNum(-1)
    assert pytest.approx(2.5) == solution.findMedian()