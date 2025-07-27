package two_sum

func twoSum(nums []int, target int) []int {
	numMap := make(map[int]int, len(nums)) // number -> index

	for idx, n := range nums {
		numMap[n] = idx
	}

	for i, n := range nums {
		remainder := target - n

		if j, ok := numMap[remainder]; ok && j != i {
			return []int{i, j}
		}
	}

	return []int{}
}
