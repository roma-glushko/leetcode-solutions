package add_two_numbers

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	result := &ListNode{}
	currNode := result

	reminder := 0

	for l1 != nil || l2 != nil {
		currNode.Next = &ListNode{}
		currNode = currNode.Next

		currNode.Val = reminder

		if l1 != nil {
			currNode.Val += l1.Val
		}

		if l2 != nil {
			currNode.Val += l2.Val
		}

		reminder = currNode.Val / 10
		currNode.Val = currNode.Val % 10

		if l1 != nil {
			l1 = l1.Next
		}

		if l2 != nil {
			l2 = l2.Next
		}
	}

	if reminder != 0 {
		currNode.Next = &ListNode{Val: reminder}
	}

	return result.Next
}
