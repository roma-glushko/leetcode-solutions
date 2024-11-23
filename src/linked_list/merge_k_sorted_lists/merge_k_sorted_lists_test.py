from typing import List
from unittest import TestCase

from .merge_k_sorted_lists import ListNode, MergeKSortedLists


class MergeKSortedListsTest(TestCase):
    def get_values_from_list(self, list_head: ListNode) -> List:
        list_values = []
        current_node = list_head

        while current_node:
            list_values.append(current_node.val)

            current_node = current_node.next

        return list_values

    def test_default_input(self):
        list_elements: List[ListNode] = [
            ListNode(1, ListNode(4, ListNode(5))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(2, ListNode(6)),
        ]

        merged_list_head = MergeKSortedLists().mergeKLists(list_elements)
        list_values = self.get_values_from_list(merged_list_head)

        self.assertEqual([1, 1, 2, 3, 4, 4, 5, 6], list_values)

    def test_empty_inputs(self):
        solution = MergeKSortedLists()

        self.assertEqual([], self.get_values_from_list(solution.mergeKLists([])))
        self.assertEqual([], self.get_values_from_list(solution.mergeKLists([[]])))
