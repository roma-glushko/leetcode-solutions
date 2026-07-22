from .merge_k_sorted_lists import ListNode, MergeKSortedLists


def get_values_from_list(list_head: ListNode) -> list:
    list_values = []
    current_node = list_head
    while current_node:
        list_values.append(current_node.val)
        current_node = current_node.next
    return list_values


def test_default_input():
    list_elements: list[ListNode] = [
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6)),
    ]
    merged_list_head = MergeKSortedLists().mergeKLists(list_elements)
    list_values = get_values_from_list(merged_list_head)
    assert [1, 1, 2, 3, 4, 4, 5, 6] == list_values


def test_empty_inputs():
    solution = MergeKSortedLists()
    assert [] == get_values_from_list(solution.mergeKLists([]))
    assert [] == get_values_from_list(solution.mergeKLists([[]]))
