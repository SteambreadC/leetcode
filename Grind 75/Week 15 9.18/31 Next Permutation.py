from typing import Optional, List
from collections import deque


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def getMax(ls:List[int]):
            return sorted(ls, reverse=True)

        for i in range(2, len(nums)+1):
            part = nums[-i:]
            if part == getMax(part):
                continue
            else:
                ns = min(x for x in part[1:] if x>part[0])
                part.remove(ns)
                ne = sorted(part)
                nums[-i:] = [ns]+ne
                return
        nums.sort()
        return


if __name__ == '__main__':
    sol = Solution()
    toPrint = sol.nextPermutation([1,1,5])
    print(toPrint)
