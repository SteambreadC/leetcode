from typing import Optional, List
from collections import deque


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i-c] + 1)
        return dp[-1] if dp[-1]<float('inf') else -1

if __name__ == '__main__':
    sol = Solution()
    toPrint = sol.coinChange([1,2,5],11)
    print(toPrint)
