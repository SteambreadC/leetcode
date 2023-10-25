from typing import Optional, List
from collections import deque


class Solution:
    def maxArea(self, height: List[int]) -> int:
        def calculateWater(i, j):
            nonlocal height
            return (j - i) * min(height[i], height[j])

        maxVal = 0
        for i in range(len(height)):
            for j in range(i, len(height)):
                val = calculateWater(i, j)
                maxVal = max(maxVal, val)
        return maxVal

    def maxArea2(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            # Calculate the area of the container formed by the two lines
            area = min(height[left], height[right]) * (right - left)

            # Update the maximum area seen so far
            max_area = max(max_area, area)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == '__main__':
    sol = Solution()
    res = sol.maxArea(["lc", "cl", "gg"])
    print(res)
