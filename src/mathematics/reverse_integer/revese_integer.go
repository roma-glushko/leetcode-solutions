package reverse_integer

import "math"

const (
	MinInt32 = math.MinInt32
	MaxInt32 = math.MaxInt32
)

func reverse(x int) int {
	var res int

	for x != 0 {
		res = res*10 + x%10
		x /= 10

		if MinInt32 > res || res > MaxInt32 {
			return 0
		}
	}

	return res
}
