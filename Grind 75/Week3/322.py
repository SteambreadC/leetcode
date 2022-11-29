from typing import Optional, List
from collections import deque


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        maxd = float('inf')
        dp = [maxd] * (amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for c in coins:
                if i>=c:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount] if dp[amount] < maxd else -1


if __name__ == '__main__':
    sol = Solution()
    res = sol.coinChange([2], 0)
    print(res)