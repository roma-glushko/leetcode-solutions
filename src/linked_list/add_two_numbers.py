class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class AddTwoNumbers:
    """
    Problem Link: https://leetcode.com/problems/add-two-numbers/
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sumhead = sumdigit = ListNode()
        subsum = 0

        while l1 is not None or l2 is not None:
            digit1 = (l1 and l1.val) or 0
            digit2 = (l2 and l2.val) or 0

            subsum = digit1 + digit2 + int(subsum >= 10)

            sumdigit.next = ListNode(subsum % 10)
            sumdigit = sumdigit.next

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        if subsum >= 10:
            sumdigit.next = ListNode(int(subsum >= 10))

        return sumhead.next
