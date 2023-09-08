from typing import Optional, List
from collections import deque


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        area = 0
        left, right = 0, len(height)-1

        while left < right:
            area = min(height[left], height[right]) * (right - left)

            maxA = max(maxA, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxA


if __name__ == '__main__':
    sol = Solution()
    res = sol.maxArea([1,8,6,2,5,4,8,3,7])
    print(res)
