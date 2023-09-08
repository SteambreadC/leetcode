from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        traverse = list()

        def inorder(p:Optional[TreeNode]):
            if not p:
                return
            inorder(p.left)
            traverse.append(p.val)
            inorder(p.right)
            return

        inorder(root)
        for i in range(len(traverse)):
            if traverse[i]>=traverse[i+1]:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    toPrint = sol.func()
    print(toPrint)
