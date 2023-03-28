from typing import Optional, List
from collections import deque


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        if S % 2 == 1:
            return False
        target = int(S / 2)
        dp = [[0 for j in range(target + 1)] for i in range(len(nums)+1)]
        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i-1][j]
                if j == nums[i - 1]:
                    dp[i][j] = 1

        return bool(dp[len(nums)][target])

    def canPartition_2(self, nums: List[int]) -> bool:
        # A simpler DP using hashmap. No need to store 2-dimensions array.
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)

        target = sum(nums) // 2

        for i in range(len(nums)):
            nextDp = set()

            for t in dp:
                if t + nums[i] == target:
                    return True
                nextDp.add(t + nums[i])
                nextDp.add(t)
            dp = nextDp
        return True if target in dp else False


if __name__ == '__main__':
    sol = Solution()
    res = sol.canPartition_2([1,5,11,5])
    print(res)
