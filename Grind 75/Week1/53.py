import string
from typing import Optional, List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum, temp = nums[0], 0
        for n in nums:
            temp = max(temp + n, n)
            sum = max(sum, temp)
        return sum
