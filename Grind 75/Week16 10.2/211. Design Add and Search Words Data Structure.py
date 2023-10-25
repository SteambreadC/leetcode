from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val: str = None, children: List = []):
        self.val = val
        self.children = children


class WordDictionary:
    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        p = self.root
        flag = 0
        for char in word:
            for child in p.children:
                if child.val == char:
                    p = child
                    flag = 1
                    break
            if flag:
                flag = 0
                continue
            else:
                q = TreeNode(char)
                p.children.append(q)
                p = q
        p.children.append(TreeNode("/"))  # The end point.
        return

    def search(self, word: str) -> bool:
        p = self.root
        pool = []
        pool.extend(p.children)
        for char in word:
            if not pool:
                break
            newpool = []
            for child in pool:
                if child.val == char or char == ".":
                    newpool.extend(child.children)
            pool = newpool
        for chd in pool:
            if chd.val == "/":
                return True
        return False


if __name__ == '__main__':
    sol = WordDictionary()
    sol.addWord("bad")
    print(len(sol.root.children))
    sol.addWord("ted")
    print(len(sol.root.children))
    print(sol.search(".ad"))
