from typing import Optional, List
from collections import deque


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        p1, p2 = 0, 0
        pos = 0

        def swap(a, b):
            nonlocal nums
            temp = nums[a]
            nums[a] = nums[b]
            nums[b] = temp
            return

        while p2 < length - 1 and p1 < length - 1:
            while nums[p1] < 1 and p1 < length - 1:
                p1 += 1
            p2 = p1
            while nums[p2] > 0 and p2 < length - 1:
                p2 += 1
            if p2 > p1:
                swap(p1, p2)
            if p2 == length:
                pos = p1
                break

        p1, p2 = pos, pos

        while p2 < length - 1 and p1 < length - 1:
            while nums[p1] < 2 and p1 < length - 1:
                p1 += 1
            p2 = p1
            while nums[p2] is not 1 and p2 < length - 1:
                p2 += 1
            if p2 > p1:
                swap(p1, p2)

        return


if __name__ == '__main__':
    sol = Solution()
    res = sol.longestPalindrome(["lc", "cl", "gg"])
    print(res)
