from typing import Optional, List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        col, row = 0, 0
        res = [0] * len(grid[0])

        for i in range(len(grid[0])):
            col = i
            row = 0
            dead = 0
            while row < len(grid) and dead == 0:
                if grid[row][col] == 1:
                    if col < len(grid[0])-1 and grid[row][col + 1] == 1:
                        col += 1
                        row += 1
                    else:
                        res[i] = -1
                        dead = 1
                elif grid[row][col] == -1:
                    if col > 0 and grid[row][col - 1] == -1:
                        col -= 1
                        row += 1
                    else:
                        res[i] = -1
                        dead = 1
            if dead == 1:
                continue
            res[i] = col
        return res
