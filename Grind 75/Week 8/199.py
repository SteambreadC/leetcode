from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightside = []
        stack = deque()
        if not root:
            return []
        pre = root.val

        stack.append(root)
        # Use -1 as a tag to show all nodes in this layer has been viewed.
        stack.append(-1)

        while stack:
            q = stack.popleft()
            if q == -1:
                rightside.append(pre)
                if not stack:
                    break
                stack.append(-1)

            else:
                pre = q.val
                if q.left:
                    stack.append(q.left)
                if q.right:
                    stack.append(q.right)
        return rightside


if __name__ == '__main__':
    sol = Solution()
    res = sol.longestPalindrome(["lc", "cl", "gg"])
    print(res)
