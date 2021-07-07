from typing import List


class ProductOfTheLastKNumbers:
    """
    Problem Link: https://leetcode.com/problems/product-of-the-last-k-numbers/
    Complexity: Medium

    Runtime: 272ms
    Memory: 29.6MB
    """
    def __init__(self):
        self.number_sequence: List[int] = []

    def add(self, num: int) -> None:
        if num == 0:
            # when 0 comes into the sequence, we can remove all preceding numbers
            # as the product would be zero
            del self.number_sequence
            self.number_sequence = []
            return

        self.number_sequence.append(
            num if len(self.number_sequence) == 0 else num * self.number_sequence[-1]
        )

    def getProduct(self, k: int) -> int:
        sequence_len: int = len(self.number_sequence)

        if sequence_len < k:
            return 0

        if k == sequence_len:
            return self.number_sequence[-1]

        return self.number_sequence[-1] // self.number_sequence[-k-1]
