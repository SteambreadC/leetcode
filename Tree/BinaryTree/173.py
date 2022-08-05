from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = list()
        self.i = -1

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.stack.append(node.val)
            inorder(node.right)

        inorder(root)

    def next(self) -> int:
        self.i += 1
        return self.stack[self.i]

    def hasNext(self) -> bool:
        return self.i < len(self.stack) - 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


if __name__ == '__main__':
    sol = Solution()
    res = sol.sortedArrayToBST([-10, -3, 0, 5, 9])
    print(res)
