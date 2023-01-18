from typing import Optional, List
from collections import deque

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = deque()

        def permuteRec(temp):
            nonlocal res
            if len(temp) == 1:
                res.append(temp)
            else:
                permuteRec(temp[0:-1])
                t = temp[-1]
                n = len(temp)
                cache = []
                while res:
                    r = res.popleft()
                    for i in range(n):
                        d = list(r)
                        d.insert(i, t)
                        cache.append(d)
                res = deque(cache)

        permuteRec(nums)

        return res

    def permute2(self, nums: List[int]) -> List[List[int]]: # Backtrack
        size = len(nums)
        res = []

        def backtrack(p:List[int]):
            nonlocal nums, size
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
