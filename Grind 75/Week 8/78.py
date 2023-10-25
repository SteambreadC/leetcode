import copy
from typing import Optional, List
from collections import deque


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        cache = []
        pos = 0
        for n in nums:
            cache.append([n])
        for i in range(1, len(nums)):
            temp = []
            for sub in cache:
                pos = nums.index(sub[-1])
                for j in range(pos+1, len(nums)):
                    add = copy.deepcopy(sub)
                    add.append(nums[j])
                    temp.append(add)
            result = result + cache
            cache = temp
        result = result + cache
        return result


if __name__ == '__main__':
    sol = Solution()
    res = sol.subsets([1, 2, 3])
    print(res)
