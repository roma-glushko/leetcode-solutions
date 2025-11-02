from heapq import heappush, heappushpop, heappop


class FindMedianFromDataStream:
    """
    Problem Link: https://leetcode.com/problems/find-median-from-data-stream/
    Complexity: Hard
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stream = None, [], []
        self.stream_part = 1

    def addNum(self, num: int) -> None:
        heappush(
            self.stream[self.stream_part],
            -heappushpop(self.stream[-self.stream_part], num * self.stream_part),
        )

        self.stream_part *= -1

    def findMedian(self) -> float:
        return 0.5 * (
            self.stream[self.stream_part][0] * self.stream_part + self.stream[-1][0]
        )


class FindMedianFromDataStreamV2:
    """
    Runtime: 155ms
    Memory: 40MB
    """
    def __init__(self):
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        if len(self.lower) > 0 and num <= -self.lower[0]:
            heappush(self.lower, -num)
        else:
            heappush(self.upper, num)

        # Balance the heaps
        if len(self.upper) > len(self.lower) + 1:
            heappush(self.lower, -heappop(self.upper))

        if len(self.lower) > len(self.upper):
            heappush(self.upper, -heappop(self.lower))

    def findMedian(self) -> float:
        if len(self.upper) > len(self.lower):
            return float(self.upper[0])

        return (-self.lower[0] + self.upper[0]) / 2.0
