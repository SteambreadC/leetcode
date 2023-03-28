from typing import Optional, List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        timer = 0
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i, j])
        queue.append([-1, -1])

        while queue:
            head = queue.popleft()
            if head[0] == -1:
                if not queue:
                    break
                else:
                    queue.append([-1, -1])
                    timer += 1
                    continue
            else:
                row, col = head[0], head[1]
                for d in directions:
                    nr, nc = row + d[0], col + d[1]
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        if grid[nr][nc] == 1:
                            queue.append([nr, nc])
                            grid[nr][nc] = 2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    timer = -1
        return timer



if __name__ == '__main__':
    sol = Solution()
    res = sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
    print(res)
