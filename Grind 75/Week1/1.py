from typing import Optional, List
from collections import deque


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i, n in enumerate(nums):
            rem = target - n
            if rem in dic.keys():
                return [dic[rem], i]
            dic[n] = i


if __name__ == '__main__':
    sol = Solution()
    res = sol.twoSum([2, 7, 11, 15], 9)
    print(res)
