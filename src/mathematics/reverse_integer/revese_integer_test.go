package reverse_integer

import (
	"fmt"
	"github.com/stretchr/testify/require"
	"testing"
)

func TestReverseInteger(t *testing.T) {
	tests := []struct {
		input int
		want  int
	}{
		{input: 123, want: 321},
		{input: -123, want: -321},
		{input: 120, want: 21},
		{input: 1534236469, want: 0},
		{input: 2000000000000, want: 2},
	}

	for _, tt := range tests {
		t.Run(fmt.Sprintf("%d", tt.input), func(t *testing.T) {
			got := reverse(tt.input)

			require.Equal(t, tt.want, got)
		})
	}
}
