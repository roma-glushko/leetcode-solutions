from typing import List, Dict


class MinStack:
    """
    Problem Link: https://leetcode.com/problems/min-stack/
    Complexity: Easy
    """
    def __init__(self):
        self.stack: List[Dict] = []

    def push(self, val: int) -> None:
        # at any given state of the stack,
        # the min value will either the current value or the min value from the prev state
        min_value: int = val

        if len(self.stack) > 0:
            min_value = min(self.stack[-1]['min'], min_value)

        self.stack.append({
            'value': val,
            'min': min_value,
        })

    def pop(self) -> None:
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]['value']

    def getMin(self) -> int:
        return self.stack[-1]['min']