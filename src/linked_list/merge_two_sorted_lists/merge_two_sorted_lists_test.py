from .merge_two_sorted_lists import ListNode, MergeTwoSortedLists


def get_values_from_list(list_head: ListNode) -> list:
    list_values = []
    current_node = list_head
    while current_node:
        list_values.append(current_node.val)
        current_node = current_node.next
    return list_values


def test_default_input():
    merged_list_head = MergeTwoSortedLists().mergeTwoLists(
        ListNode(1, ListNode(2, ListNode(4))),
        ListNode(1, ListNode(3, ListNode(4))),
    )
    list_values = get_values_from_list(merged_list_head)
    assert [1, 1, 2, 3, 4, 4] == list_values
