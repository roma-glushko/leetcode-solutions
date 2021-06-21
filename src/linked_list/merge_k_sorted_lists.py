from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MergeKSortedLists:
    """
    Problem Link: https://leetcode.com/problems/merge-k-sorted-lists/
    Complexity: Hard
    Possible Solutions:
        - Convert given lists in the array. Sort it and build a new list from it.
            Runtime: O(p*log(p) + 2p), Memory: O(2p) where p is a total number of elements in all k-lists
        - Build a heap from the all elements and then build a list by extracting min elements
            Runtime: O(2p*log(p)), Memory: O(p)
        - Merge lists in a merge sort manner: get every two lists merged and then proceed merging newly created lists
            until there is only one list that consists of all elements
            Runtime: O(n*log(k)), Memory: O(1)?
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        list_num: int = len(lists)

        if list_num == 1:
            return lists[0]  # retrieve the head node

        list_mid_idx: int = list_num // 2

        return self.merge(
            self.mergeKLists(lists[:list_mid_idx]),  # left subarray
            self.mergeKLists(lists[list_mid_idx:]),  # right subarray
        )

    def merge(self, list1: ListNode, list2: ListNode) -> ListNode:
        """
        Merge two lists in O(min(len(list1), len(list2))) time via two pointers
        """
        merged_list_head = merged_list = ListNode(0)

        node1: ListNode = list1
        node2: ListNode = list2

        while node1 and node2:
            if node1.val < node2.val:
                merged_list.next = node1

                node1 = node1.next
                merged_list = merged_list.next

                continue

            merged_list.next = node2

            merged_list = merged_list.next
            node2 = node2.next

        # handle remaining nodes if one of the lists is shorted than another
        # 1 -> 2 -> 3 -> 4
        # 1 -> 2

        if node1:
            merged_list.next = node1

        if node2:
            merged_list.next = node2

        return merged_list_head.next