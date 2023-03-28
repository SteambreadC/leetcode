from typing import Optional, List
from collections import deque


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        leftPro, rightPro = 1, 1
        for i in range(len(nums)):
            answer.append(leftPro)
            leftPro = leftPro * nums[i]
        for i in range(len(nums)):
            answer[len(nums) - i - 1] = answer[len(nums) - i - 1] * rightPro
            rightPro = rightPro * nums[-i-1]
        return answer


if __name__ == '__main__':
    sol = Solution()
    res = sol.productExceptSelf([-1,1,0,-3,3])
    print(res)
