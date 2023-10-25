from typing import Optional, List
import math
from collections import deque

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        res = []

        def backtrack(p:List[int]):
            nonlocal nums
            if len(p) == size:
                res.append(list(p))
                return
            for i in nums:
                if i not in p:
                    p.append(i)
                    backtrack(p)
                    p.pop()

        backtrack([])
        return res


if __name__ == '__main__':
    sol = Solution()
    res = sol.permute([1,2,3])
    print(res)
