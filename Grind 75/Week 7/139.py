from typing import Optional, List
from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * (len(s) + 1)
        dp[0] = 1

        for i in range(0, len(s) + 1):
            for j in range(0, i):
                if dp[j] > 0 and (s[j:i] in wordDict):
                    dp[i] = 1

        return bool(dp[len(s)])

if __name__ == '__main__':
    sol = Solution()
    res = sol.wordBreak("applepenapple",["apple","pen"])
    print(res)
