from typing import Optional, List


# Definition for a Node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0 # Use global variable to track diameter in the whole process of calculating. THE POINT.

        def calculDepth(tRoot: Optional[TreeNode]) -> int:
            nonlocal diameter
            if not tRoot:
                return 0

            leftD = calculDepth(tRoot.left)
            rightD = calculDepth(tRoot.right)
            diameter = max(diameter, leftD + rightD)
            return max(leftD, rightD) + 1

        if not root:
            return 0
        else:
            calculDepth(root)
            return diameter
