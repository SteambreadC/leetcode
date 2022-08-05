from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest_nonRecursion(self, root: Optional[TreeNode], k: int) -> int:
        p = root
        inorder = list()
        while True:
            if p:
                inorder.append(p)
                p = p.left
            else:
                p = inorder.pop()
                k -= 1
                if k == 0:
                    return p.val
                p = p.right
        return -1

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0

        def kthInorder(node):
            nonlocal k, res
            if k == 0:
                return
            if not node:
                return
            kthInorder(node.left)
            k -= 1
            if k == 0:
                res = node.val
                return
            kthInorder(node.right)

        kthInorder(root)
        return res


if __name__ == '__main__':
    sol = Solution()
    res = sol.sortedArrayToBST([-10, -3, 0, 5, 9])
    print(res)
