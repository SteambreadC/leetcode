from typing import Optional, List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = grid
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        stack = deque()
        islands = 0

        def DFS():
            while stack:
                q = stack.pop()
                for d in directions:
                    new =[0, 0]
                    new[0] = q[0] + d[0]
                    new[1] = q[1] + d[1]
                    if not (0 <= new[0] < len(grid) and 0 <= new[1] < len(grid[0])):
                        continue
                    elif grid[new[0]][new[1]] == "1":
                        stack.append([new[0], new[1]])
                        grid[new[0]][new[1]] = "2"

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    stack.append([i, j])
                    islands += 1
                    grid[i][j] = "2"
                    DFS()
        return islands


if __name__ == '__main__':
    sol = Solution()
    res = sol.numIslands(
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]])
    print(res)
