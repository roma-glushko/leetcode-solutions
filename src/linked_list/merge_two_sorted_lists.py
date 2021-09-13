class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MergeTwoSortedLists:
    """
    Problem Link: https://leetcode.com/problems/merge-two-sorted-lists/
    Complexity: Easy
    Runtime: 24ms
    Memory: 14.4MB
    """

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merged_list_head = current_head = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                current_head.next = l1

                l1 = l1.next
                current_head = current_head.next
                continue

            current_head.next = l2
            l2 = l2.next
            current_head = current_head.next

        if l1:
            current_head.next = l1

        if l2:
            current_head.next = l2

        return merged_list_head.next
