from typing import Optional, List
from collections import deque


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        mid = int((left + right) / 2)
        while left < right:
            if nums[mid] == target:
                return mid
            else:
                if nums[left] <= nums[mid]:
                    if nums[left] <= target < nums[mid]:
                        right = mid - 1
                        mid = int((left + right) / 2)
                        continue
                    else:
                        left = mid + 1
                        mid = int((left + right) / 2)
                        continue
                if nums[right] >= nums[mid]:
                    if nums[mid] < target <= nums[right]:
                        left = mid + 1
                        mid = int((left + right) / 2)
                        continue
                    else:
                        right = mid - 1
                        mid = int((left + right) / 2)
                        continue
        if nums[left] == target:
            return left
        else:
            return -1


if __name__ == '__main__':
    sol = Solution()
    res = sol.search([5, 3], 0)
    print(res)
