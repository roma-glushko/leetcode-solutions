from unittest import TestCase

from .middle_of_the_linked_list import ListNode, MiddleOfTheLinkedList


class MiddleOfTheLinkedListTest(TestCase):
    def test_default_inputs(self):
        solution = MiddleOfTheLinkedList()

        self.assertEqual(
            3,
            solution.middleNode(
                ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
            ).val,
        )

        self.assertEqual(
            4,
            solution.middleNode(
                ListNode(
                    1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))
                )
            ).val,
        )
