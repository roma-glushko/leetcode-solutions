from typing import List


class BestTimeToBuyAndSellStock:
    """
    Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    Complexity: Easy
    """
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0
        day = 1

        while day < len(prices):
            current_price = prices[day]

            profit = max(profit, current_price - buy_price)
            buy_price = min(buy_price, current_price)

            day += 1

        return profit