from typing import Optional, List
from collections import deque
import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m+n-2,m-1)


if __name__ == '__main__':
    sol = Solution()
    res = sol.longestPalindrome(["lc", "cl", "gg"])
    print(res)
