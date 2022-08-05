from typing import Optional, List


# Definition for a Node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def pathStartHere(node, target):
            res = 0
            if not node:
                return 0
            if target == node.val:
                res = 1
            return pathStartHere(node.left, target - node.val) + pathStartHere(node.right, target - node.val) + res

        if not root:
            return 0
        return pathStartHere(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

    def pathSum2_prefixSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def preorder(node, currSum):
            nonlocal count
            if not node:
                return
            currSum += node.val
            if currSum == k:
                count += 1
            if h.get(currSum - k):
                count += h[currSum - k]
            if h.get(currSum):
                h[currSum] += 1
            else:
                h[currSum] = 1
            preorder(node.left, currSum)
            preorder(node.right, currSum)
            h[currSum] -= 1

        k = targetSum
        count = 0
        h = dict()
        preorder(root, 0)
        return count
