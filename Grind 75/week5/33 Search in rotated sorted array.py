from typing import Optional, List
from collections import deque


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 重点是：rotated list的前半段与后半段依然是rotated list，满足特征
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[mid] > target >= nums[left]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
        return -1


if __name__ == '__main__':
    sol = Solution()
    toPrint = sol.search([4, 5, 6, 7, 0, 1, 2], 5)
    print(toPrint)
