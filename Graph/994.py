from typing import Optional, List
import collections


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = False
        rottenList = list()
        rotCount = 0

        def rot(i, j):
            nonlocal grid
            if i > 0:
                grid[i - 1][j] = 2 if grid[i - 1][j] >= 1 else 0
            if j > 0:
                grid[i][j - 1] = 2 if grid[i][j - 1] >= 1 else 0
            if i < len(grid) - 1:
                grid[i + 1][j] = 2 if grid[i + 1][j] >= 1 else 0
            if j < len(grid[0]) - 1:
                grid[i][j + 1] = 2 if grid[i][j + 1] >= 1 else 0

        while True:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        fresh = True
                    if grid[i][j] == 2:
                        rottenList.append([i, j])
            if not fresh:
                return time
            for pos in rottenList:
                rot(pos[0], pos[1])
            if len(rottenList) == rotCount:
                return -1
            rotCount = len(rottenList)
            rottenList.clear()
            fresh = False
            time += 1

    def orangesRotting2_BFS(self, grid: List[List[int]]) -> int:
        time = -1
        rottenList = collections.deque()
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    rottenList.append([i, j])

        rottenList.append([-1, -1])

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while rottenList:
            i, j = rottenList.popleft()
            if i == -1:
                time += 1
            else:
                for d in directions:
                    nextI, nextJ = i + d[0], j + d[1]
                    if 0<=nextI<len(grid) and 0<=nextJ<len(grid[0]):
                        if grid[nextI][nextJ] == 1:
                            grid[nextI][nextJ]=2
                            fresh -= 1
                            rottenList.append([nextI,nextJ])

        return time if fresh==0 else -1


if __name__ == '__main__':
    sol = Solution()
    res = sol.longestPalindrome(["lc", "cl", "gg"])
    print(res)
