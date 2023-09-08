from typing import Optional, List
from collections import deque, defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0] * numCourses
        checked = [0] * numCourses
        tag = True
        dic = defaultdict(set)
        for i in prerequisites:
            dic[i[0]].add(i[1])

        def DFS(j):
            nonlocal tag, visited, checked
            if checked[j] == 1:
                return
            if visited[j] == 1:
                tag = False
                return
            else:
                visited[j] = 1
                for k in dic[j]:
                    DFS(k)
                visited[j] = 0
                checked[j] = 1

        for i in range(numCourses):
            DFS(i)
            if not tag:
                return tag
        return tag


if __name__ == '__main__':
    sol = Solution()
    toPrint = sol.canFinish(5, [[1,4],[2,4],[3,1],[3,2]])
    print(toPrint)
