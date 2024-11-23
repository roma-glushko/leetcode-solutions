# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MiddleOfTheLinkedList:
    """
    Problem Link: https://leetcode.com/problems/middle-of-the-linked-list/
    Complexity: Easy

    Runtime: 28ms
    Memory: 14.3MB
    """

    def middleNode(self, head: ListNode) -> ListNode:
        """
        Solution leverages an idea of fast and slow pointers.
        Fast pointer goes two times faster than the slow one.
        Once the fast pointer reach the end of the list, the slow one must be
        somewhere in a middle of the list
        """
        fast_pointer, slow_pointer = head, head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return slow_pointer
