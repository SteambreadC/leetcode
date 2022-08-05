from typing import Optional, List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        left = 0
        mid = (left + right) / 2
        while left < right:
            if nums(mid) == target:
                return mid
            elif nums(mid) < target:
                left = mid + 1
                mid = (left + right) / 2
            elif nums(mid) > target:
                right = mid - 1
                mid = (left + right) / 2
        return -1


if __name__ == '__main__':
    print('PyCharm')
