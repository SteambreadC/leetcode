from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def subBalanced(subRoot: Optional[TreeNode]) -> [bool, int]:
            if not subRoot:
                return [True, 0]
            leftRes = subBalanced(subRoot.left)
            rightRes = subBalanced(subRoot.right)
            isb = leftRes[0] and rightRes[0]
            height = max(leftRes[1], rightRes[1]) + 1
            if leftRes[1] > rightRes[1] + 1 or leftRes[1] < rightRes[1] - 1:
                isb = False
            return [isb, height]

        res = subBalanced(root)[0]
        return res

if __name__ == '__main__':
   sol = Solution()
   res = sol.isBalanced([3,9,20,null,null,15,7])
   print(res)