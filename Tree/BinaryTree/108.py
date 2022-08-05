from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        left = 0
        right = len(nums) - 1
        mid = int((left + right) / 2)
        root = TreeNode()
        root.val = nums[mid]
        if mid > left:
            root.left = self.sortedArrayToBST(nums[0:mid])
        if mid < right:
            root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


if __name__ == '__main__':
    sol = Solution()
    res = sol.sortedArrayToBST([-10, -3, 0, 5, 9])
    print(res)
