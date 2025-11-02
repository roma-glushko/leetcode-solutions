import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone_weight1, stone_weight2 = -heapq.heappop(stones), -heapq.heappop(stones)

            if stone_weight1 != stone_weight2:
                new_stone_weight = abs(stone_weight1 - stone_weight2)

                heapq.heappush(stones, -new_stone_weight)

        if not stones:
            return 0

        return -stones[0]


if __name__ == "__main__":
    solution = Solution()
    stones = [2,7,4,1,8,1]
    # stones = [2,2] testcase 2
    print(solution.lastStoneWeight(stones))  # Output: 1
