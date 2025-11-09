class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0 # base case: it takes 0 coins to make amount 0

        for amount in range(1, amount + 1):
            for coin in coins:
                if amount >= coin:
                    dp[amount] = min(dp[amount], 1 + dp[amount - coin])

        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == "__main__":
    solution = Solution()
    coins = [1, 4, 5]
    amount = 8
    print(solution.coinChange(coins, amount))  # Output: 3 (11 = 5 + 5 + 1)