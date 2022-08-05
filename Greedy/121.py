from typing import Optional, List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = float('inf')
        size = len(prices)
        for i in range(size):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > profit:
                profit = prices[i] - min_price
        return profit
