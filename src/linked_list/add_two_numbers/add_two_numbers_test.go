package add_two_numbers

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func TestAddTwoNumbers(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name   string
		l1, l2 *ListNode
		want   []int
	}{
		{
			name: "testcase1",
			l1:   makeList(2, 4, 3),
			l2:   makeList(5, 6, 4),
			want: []int{7, 0, 8},
		},
		{
			name: "testcase2",
			l1:   makeList(0),
			l2:   makeList(0),
			want: []int{0},
		},
		{
			name: "testcase3",
			l1:   makeList(9, 9, 9, 9, 9, 9, 9),
			l2:   makeList(9, 9, 9, 9),
			want: []int{8, 9, 9, 9, 0, 0, 0, 1},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			gotList := addTwoNumbers(tt.l1, tt.l2)

			got := make([]int, 0, len(tt.want))

			for gotList != nil {
				got = append(got, gotList.Val)
				gotList = gotList.Next
			}

			require.Equal(t, tt.want, got)
		})
	}
}

func makeList(vals ...int) *ListNode {
	head := &ListNode{Val: vals[0], Next: nil}
	curr := head

	for _, val := range vals[1:] {
		curr.Next = &ListNode{Val: val, Next: nil}
		curr = curr.Next
	}

	return head
}
