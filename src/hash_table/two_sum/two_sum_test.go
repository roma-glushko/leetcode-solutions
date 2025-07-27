package two_sum

import (
	"github.com/stretchr/testify/require"
	"testing"
)

func TestTwoSum(t *testing.T) {
	t.Parallel()

	tests := []struct {
		nums    []int
		target  int
		wantIdx []int
	}{
		{nums: []int{2, 7, 11, 15}, target: 9, wantIdx: []int{0, 1}},
		{nums: []int{3, 2, 4}, target: 6, wantIdx: []int{2, 1}},
		{nums: []int{3, 3}, target: 6, wantIdx: []int{0, 1}},
	}

	for _, tt := range tests {
		t.Run("", func(t *testing.T) {
			got := twoSum(tt.nums, tt.target)

			for _, v := range got {
				require.Contains(t, tt.wantIdx, v)
			}
		})
	}
}
