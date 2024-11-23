from heapq import heappush, heappushpop


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
