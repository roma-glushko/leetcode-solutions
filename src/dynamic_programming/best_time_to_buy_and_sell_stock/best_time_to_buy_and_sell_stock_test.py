from .best_time_to_buy_and_sell_stock import BestTimeToBuyAndSellStock


def test_default_input():
    solution = BestTimeToBuyAndSellStock()
    perimeter = solution.maxProfit([7, 1, 5, 3, 6, 4])
    assert perimeter == 5
