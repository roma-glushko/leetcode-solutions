from unittest import TestCase

from .best_time_to_buy_and_sell_stock import BestTimeToBuyAndSellStock


class BestTimeToBuyAndSellStockTest(TestCase):

    def test_default_input(self):
        solution = BestTimeToBuyAndSellStock()
        perimeter = solution.maxProfit([7, 1, 5, 3, 6, 4])

        self.assertEqual(perimeter, 5)
