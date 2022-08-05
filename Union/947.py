from typing import Optional, List
from collections import deque, defaultdict


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        dictC = defaultdict(set)
        dictR = defaultdict(set)
        stack = deque()
        maxC, maxR, remove = 0, 0, 0
        for s in stones:
            maxC = max(maxC, s[1])
            maxR = max(maxR, s[0])
            dictC[s[1]].add(tuple(s))
            dictR[s[0]].add(tuple(s))

        visitedR = [0] * (maxR + 1)
        visitedC = [0] * (maxC + 1)

        for s in stones:
            if visitedR[s[0]] > 0 or visitedC[s[1]] > 0:
                continue
            stack.append(s)
            while stack:
                q = stack.popleft()
                if visitedR[q[0]] == 0:
                    visitedR[q[0]] = 1
                    for p in dictR[q[0]]:
                        if visitedC[p[1]] == 0 and p != tuple(q):
                            stack.append(p)
                            remove += 1
                if visitedC[q[1]] == 0:
                    visitedC[q[1]] = 1
                    for p in dictC[q[1]]:
                        if visitedR[p[0]] == 0 and p != tuple(q):
                            stack.append(p)
                            remove += 1
        return remove


if __name__ == '__main__':
    sol = Solution()
    res = sol.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]])
    print(res)
