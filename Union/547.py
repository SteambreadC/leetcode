from typing import Optional, List
from collections import deque


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        visited = [0 for i in range(size)]
        stack = deque()
        num = 0
        for i in range(size):
            if visited[i] == 1:
                continue
            stack.append(i)
            while stack:
                q = stack.popleft()
                for j in range(size):
                    if isConnected[q][j] == 1 and visited[j] == 0:
                        stack.append(j)
                        visited[j] = 1
            num += 1

        return num


if __name__ == '__main__':
    sol = Solution()
    res = sol.findCircleNum([[1, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 1], [0, 0, 1, 1]])
    print(res)
