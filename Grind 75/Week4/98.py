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
        def checkChild(n: Optional[TreeNode]) -> dict:
            checkRes = dict()
            if not n:
                return dict(res=True, minV=float('inf'), maxV=-float('inf'))
            if (not n.left) and (not n.right):
                return dict(res=True, minV=n.val, maxV=n.val)

            left = checkChild(n.left)
            right = checkChild(n.right)
            temp = left.get('res') and right.get('res') and left.get('maxV') < n.val < right.get('minV')
            checkRes['res'] = temp
            checkRes['maxV'] = max(n.val, right.get('maxV'))
            checkRes['minV'] = min(n.val, left.get('minV'))
            return checkRes

        dic = checkChild(root)
        return dic['res']

if __name__ == '__main__':
    sol = Solution()
    res = sol.isValidBST([2, 1, 3])
    print(res)
