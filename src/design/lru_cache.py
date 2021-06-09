from typing import Dict


class LRUCache:
    """
    Problem Link: https://leetcode.com/problems/lru-cache/
    Complexity: Medium
    """
    capacity: int = 1
    cache_map: Dict[int, int] = {}

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache_map:
            return -1

        return self.cache_map[key]

    def put(self, key: int, value: int) -> None:
        self.cache_map[key] = value