"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        queue = deque()
        queue.append(node)
        queueNew = deque()
        queueNew.append(Node(node.val, []))
        visited = list()
        resList = list()
        while queue:
            p = queue.popleft()
            n = queueNew.popleft()
            if p in visited:
                continue
            visited.append(p)
            nerghbor = []
            for q in p.neighbors:
                if q in visited:
                    continue
                print(q.val)
                queue.append(q)
                t = Node(q.val, [])
                queueNew.append(t)
                n.neighbors.append(t)
                t.neighbors.append(n)
            resList.append(n.neighbors)
        return resList
