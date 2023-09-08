from typing import Optional, List
from collections import deque, defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        degrees = defaultdict(set)
        res = []
        backup = []
        if not edges:
            return 0
        for e in edges:
            a,b = e[0],e[1]
            degrees[a].add(b)
            degrees[b].add(a)

        while degrees:
            for k in degrees.keys():
                if len(degrees[k]) <= 1:
                    backup.append(k)
            for k in backup:
                degrees.pop(k)
                for n in degrees.keys():
                    if k in degrees[n]:
                        degrees[n].remove(k)
            res = backup
            backup = []

        return res




if __name__ == '__main__':
    sol = Solution()
    res = sol.findMinHeightTrees(1,[])
    print(res)
