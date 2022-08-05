from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = list()
        nodes= list()
        if not root:
            return res
        nodes.append([root])
        res.append([root.val])
        lv = 0
        while lv<len(nodes):
            ls = []
            ls_val=[]
            for p in nodes[lv]:
                if p.left:
                    ls.append(p.left)
                if p.right:
                    ls.append(p.right)
            if ls:
                 nodes.append(ls)
                 for i in ls:
                    ls_val.append(i.val)
                 res.append(ls_val)
            lv += 1
        return res


if __name__ == '__main__':
    sol = Solution()
