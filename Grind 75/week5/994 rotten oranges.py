from typing import Optional, List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rList = deque()
        time = -1
        fresh = 0
        newtag = 0
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rList.append([i, j])
        rList.append([-1, -1])
        while rList:
            q = rList.popleft()
            if q[0] == -1:
                time += 1
                if newtag == 1:
                    rList.append([-1, -1])
                    newtag = 0
                else:
                    break
                continue
            else:
                for d in directions:
                    newC, newR = q[0] + d[0], q[1] + d[1]
                    if 0 <= newC < len(grid) and 0 <= newR < len(grid[0]):
                        if grid[newC][newR] == 1:
                            rList.append([newC, newR])
                            grid[newC][newR] = 2
                            newtag = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh = 1

        return time if fresh == 0 else -1


if __name__ == '__main__':
    sol = Solution()
    toPrint = sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
    print(toPrint)
