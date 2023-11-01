from copy import copy, deepcopy
from typing import Optional, List
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights[0]), len(heights)
        P = [[0 for i in range(len(heights[0]))] for j in range(len(heights))]
        A = deepcopy(P)
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        res = []

        def dfs(i, j, matrix):
            if matrix[i][j] >= 1:
                return
            else:
                matrix[i][j] = 1
                for d in directions:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < n and 0 <= nj < m:
                        if heights[i][j] <= heights[ni][nj]:
                            dfs(ni, nj, matrix)

        for j in range(m):
            dfs(0, j, P)
            dfs(n-1, j, A)
        for i in range(n):
            dfs(i, 0, P)
            dfs(i, m-1, A)
        for i in range(n):
            for j in range(m):
                if P[i][j] == 1 and A[i][j] == 1:
                    res.append([i, j])
        return res


if __name__ == '__main__':
    sol = Solution()
    res = sol.pacificAtlantic([[1,1], [1,1], [1,1]])
    print(res)
