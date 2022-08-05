from typing import Optional, List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        offset = 0
        length = len(nums)
        originList = list()
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                offset = length - i - 1
                break
        for i in range(offset):
            originList.append(nums[-offset + i])
        for i in range(length - offset):
            originList.append(nums[i])
        left = 0
        right = length - 1
        while left <= right:
            mid = int((left + right) / 2)
            if originList[mid] == target:
                return (mid - offset) % length
            if originList[mid] > target:
                right = (mid - 1)
            else:
                left = (mid + 1)
        return -1

    def search2_onetimesearch(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


if __name__ == '__main__':
    sol = Solution()
    res = sol.search([3, 5, 1], 5)
    print(res)
