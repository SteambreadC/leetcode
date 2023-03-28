from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
import null as null


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = TreeNode(-1)

        def isChild(node: 'TreeNode'):
            nonlocal lca
            result = 0
            if not node:
                return False
            if lca.val != -1:
                return False
            if node.val == p.val or node.val == q.val:
                result = True
            left = isChild(node.left)
            right = isChild(node.right)
            if result + left + right >= 2:
                lca = node
            return result or left or right

        isChild(root)
        return lca


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    res = sol.lowestCommonAncestor(root, TreeNode(1), TreeNode(2))
    print(res.val)
