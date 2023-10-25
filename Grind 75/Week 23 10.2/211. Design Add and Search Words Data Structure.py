from typing import List


class TreeNode:
    def __init__(self, val: str = None, children: 'List[TreeNode]' = None):
        self.val = val
        self.children = {}
        self.end = False


class WordDictionary:
    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        p = self.root
        for char in word:
            if char not in p.children:
                q = TreeNode(char)
                p.children[char] = q
            p = p.children[char]
        p.end = True  # The end point.
        return


    def search(self, word: str) -> bool:
        p = self.root
        pool = [p]
        for index, char in enumerate(word):
            newpool = []
            for child in pool:
                if char == '.':
                    newpool.extend(child.children.values())
                elif char in child.children:
                    newpool.append(child.children[char])
            if not newpool:
                return False
            pool = newpool
        return any(child.end for child in pool)


if __name__ == '__main__':
    sol = WordDictionary()
    sol.addWord("a")
    print(len(sol.root.children))
    sol.addWord("ab")
    print(len(sol.root.children))
    print(sol.search("a"))
