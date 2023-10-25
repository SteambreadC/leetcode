class Trie:

    def __init__(self):
        self.root = Node(0, [])

    def insert(self, word: str) -> None:
        prev = self.root
        n = Node(0, [])
        tag = 0
        for c in word:
            for n in prev.children:
                if c == n.val:
                    prev = n
                    tag = 1
                    break
            if tag == 1:
                tag = 0
                continue
            node = Node(c, [])
            prev.children.append(node)
            prev = node
        prev.end = True

    def search(self, word: str) -> bool:
        prev = self.root
        n = Node()
        tag = 0
        for c in word:
            for n in prev.children:
                if c == n.val:
                    prev = n
                    tag = 1
                    break
            if tag == 0:
                return False
            tag = 0
        return prev.end

    def startsWith(self, prefix: str) -> bool:
        prev = self.root
        n = Node()
        tag = 0
        for c in prefix:
            for n in prev.children:
                if c == n.val:
                    prev = n
                    tag = 1
                    break
            if tag == 0:
                return False
            tag = 0
        return True


class Node:
    def __init__(self, val=0, children=None, end=False):
        self.val = val
        self.children = children
        self.end = end


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
if __name__ == '__main__':
    obj = Trie()
    obj.insert('apple')
    print(obj.search('apple'))


''' 2nd try 
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        r = self.root
        tag = 0
        
        for c in word:
            for t in r.children:
                if t.val == c:
                    r = t
                    tag = 1
                    break
            if tag == 1:
                tag = 0
                continue
            p = Node(c)
            r.children.add(p)
            r = p
            tag = 0
        r.end = 1
        

    def search(self, word: str) -> bool:
        r = self.root
        tag = 0
        for c in word:
            for t in r.children:
                if t.val == c:
                    r = t
                    tag = 1
                    break
            if tag == 0:
                return False
            else:
                tag = 0
                continue
        if r.end:
            return True
        else:
            return False
            
                

    def startsWith(self, prefix: str) -> bool:
        r = self.root
        tag = 0
        if len(r.children)<1:
            return False
        for c in prefix:
            for t in r.children:
                if t.val == c:
                    r = t
                    tag = 1
                    break
            if tag == 0:
                return False
            tag = 0
        if r.end:
            return False
        else:
            return True
    
class Node:
    def __init__(self,val = 0, children = set(), end = 0):
        self.val = val
        self.children = children
        self.end = end


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
'''