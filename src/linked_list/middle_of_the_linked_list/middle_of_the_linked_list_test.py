from .middle_of_the_linked_list import ListNode, MiddleOfTheLinkedList


def test_default_inputs():
    solution = MiddleOfTheLinkedList()
    assert (
        3
        == solution.middleNode(
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        ).val
    )
    assert (
        4
        == solution.middleNode(
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
        ).val
    )
