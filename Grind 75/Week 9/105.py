from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def recurBuildTree(preorder, inorder):
            if not preorder or not inorder:
                return None

            # The first element of the preorder traversal is the root node
            root_val = preorder[0]
            root = TreeNode(root_val)

            # Find the index of the root node in the inorder traversal
            root_index = inorder.index(root_val)

            # Recursively construct the left and right subtrees
            root.left = recurBuildTree(preorder[1:root_index + 1], inorder[:root_index])
            root.right = recurBuildTree(preorder[root_index + 1:], inorder[root_index + 1:])

            return root

        return recurBuildTree(preorder, inorder)


if __name__ == '__main__':
    sol = Solution()
    res = sol.buildTree([3, 9, 6, 12, 20, 15, 7], [6, 9, 12, 3, 15, 20, 7])
    print(res)
