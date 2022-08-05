from typing import Optional, List
import collections
import queue


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumN = sum(nums)
        if sumN % 2 == 1:
            return False
        half = int(sumN / 2)
        n = len(nums)
        dp = [[False] * (half + 1) for i in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            cur = nums[i - 1]
            for j in range(half + 1):
                if j < cur:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - cur]
        return dp[-1][half]


if __name__ == '__main__':
    sol = Solution()
    res = sol.canPartition([1, 5, 5, 11])
    print(res)
