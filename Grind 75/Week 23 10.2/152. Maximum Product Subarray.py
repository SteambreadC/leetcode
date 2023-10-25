from typing import Optional, List
from collections import deque

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        keens, steakhouse = 1, 1
        maxProduct = nums[0]
        for n in nums:
            keensT = max(keens*n, steakhouse*n, n)
            steakhouse = min(keens * n, steakhouse*n, n)
            keens = keensT
            maxProduct = max(maxProduct, keens)
        return maxProduct



if __name__ == '__main__':
    sol = Solution()
    toPrint = sol.maxProduct()
    print(toPrint)
