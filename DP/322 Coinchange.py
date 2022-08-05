from typing import Optional, List
import collections
import queue


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # This problem use double dynamic programming, for coin and amount.
        # The bottom-up method.
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] < float('inf') else -1
