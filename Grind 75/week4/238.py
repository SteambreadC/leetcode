from typing import Optional, List
from collections import deque


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = list()
        pre, suf = 1, 1
        answer.append(1)
        for i in range(1, len(nums)):
            temp = answer[i-1] * nums[i-1]
            answer.append(temp)
        temp = 1
        for j in range(len(nums)-2, -1, -1):
            temp = temp * nums[j+1]
            answer[j] = answer[j] * temp
        return answer


if __name__ == '__main__':
    sol = Solution()
    toPrint = sol.productExceptSelf([1,2,3,4])
    print(toPrint)
