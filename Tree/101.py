from typing import Optional, List
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        leftList, rightList = list(), list()

        def traverse(node, tag):
            nonlocal leftList, rightList
            if not node:
                return
            if tag == 1:
                if not node.left:
                    leftList.append(200)
                if not node.right:
                    leftList.append(-200)
                traverse(node.left, 1)
                leftList.append(node.val)
                traverse(node.right, 1)
            else:
                if not node.right:
                    rightList.append(200)
                if not node.left:
                    rightList.append(-200)
                traverse(node.right, 0)
                rightList.append(node.val)
                traverse(node.left, 0)
        traverse(root.left, 1)
        traverse(root.right, 0)
        return rightList == leftList


if __name__ == '__main__':
    sol = Solution()
    res = sol.isSymmetric()
    print(res)
