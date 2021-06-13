from typing import Dict, Optional


class Node:
    def __init__(self, key: int, value: int, prev=None, next=None):
        self.key: int = key
        self.value: int = value

        self.prev: Optional[Node] = prev
        self.next: Optional[Node] = next


class LinkedList:
    head: Optional[Node] = None
    tail: Optional[Node] = None

    def add_to_head(self, item: Node):
        if self.head is not None:
            item.next = self.head
            self.head.prev = item

        if self.tail is None:
            self.tail = item

        self.head = item

    def unlink(self, item: Node):
        if item is None:
            return

        prev_item: Node = item.prev
        next_item: Node = item.next

        # unlink the item node:
        # link prev and next items
        # removing referenced to the current item node
        if prev_item is not None:
            prev_item.next = next_item

        if next_item is not None:
            next_item.prev = prev_item

        if self.head == item:
            # item was the first element in the list
            self.head = next_item

        if self.tail == item:
            # item was the last element in the list
            self.tail = prev_item

        item.prev = None
        item.next = None


class LRUCache:
    """
    Problem Link: https://leetcode.com/problems/lru-cache/
    Complexity: Medium
    """
    capacity: int
    cache_map: Dict[int, Node]
    history: LinkedList

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_map = {}
        self.history = LinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache_map:
            return -1

        value_node: Node = self.cache_map[key]

        if self.history.head != value_node:
            # make item the most recently used
            self.history.unlink(value_node)
            self.history.add_to_head(value_node)

        return value_node.value

    def put(self, key: int, value: int) -> None:
        value_node: Node = Node(key, value)

        if key in self.cache_map:
            self.remove_item(self.cache_map[key])

        if len(self.cache_map) >= self.capacity:
            # no space left, needs to evict the least recently used item
            self.evict_least_recent_item()

        self.history.add_to_head(value_node)
        self.cache_map[key] = value_node

    def evict_least_recent_item(self):
        lru_item: Node = self.history.tail

        if lru_item is None:
            return

        self.remove_item(lru_item)

    def remove_item(self, item: Node):
        self.history.unlink(item)

        del self.cache_map[item.key]
        del item
