from typing import Optional, List
from collections import deque


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        left, right = [0] * n, [0] * n
        left[0] = nums[0]
        right[n - 1] = nums[-1]
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i]
            right[n - i - 1] = right[n - i] * nums[n - i - 1]
        for i in range(1, n - 1):
            ans[i] = left[i - 1] * right[i + 1]
        ans[0] = right[1]
        ans[n - 1] = left[n - 2]
        return ans



if __name__ == '__main__':
    sol = Solution()
    res = sol.productExceptSelf([1, 2, 3, 4])
    print(res)
