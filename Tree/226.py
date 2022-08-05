class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        tempNode=root.right
        root.right=root.left
        root.left=tempNode
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root