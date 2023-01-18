from typing import Optional, List
from collections import deque


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(remain, comb, pos):
            if remain == 0:
                results.append(list(comb))  # Use list to make a copy here.
                return
            if remain < 0:
                return

            for i in range(pos, len(candidates)):
                comb.append(candidates[i])
                backtrack(remain - candidates[i], comb, i)
                comb.pop()

        backtrack(target, [], 0)
        return results


if __name__ == '__main__':
    sol = Solution()
    res = sol.combinationSum([2,3,6,7], 7)
    print(res)
