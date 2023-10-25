from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ls = [-1]
        def inorder(p:Optional[TreeNode]):
            nonlocal ls
            if not p:
                return None
            inorder(p.left)
            ls.append(p.val)
            inorder(p.right)
        inorder(root)
        return ls[k]





if __name__ == '__main__':
    sol = Solution()
    res = sol.longestPalindrome(["lc", "cl", "gg"])
    print(res)
