from typing import Optional, List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        p = root
        res = list()

        def traverse_rec(ptr: Node) -> None:
            res.append(ptr.val)
            for chd in ptr.children:
                traverse_rec(chd)

        if p is None:
            return res
        else:
            traverse_rec(p)
        return res
