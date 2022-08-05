from typing import Optional, List
import collections


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def toOcean(row, col):
            nonlocal heights, resList
            visited = [[0] * len(heights[0]) for t in range(len(heights))]
            directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            pac, atl = 0, 0
            queue = collections.deque()
            queue.append([row, col])

            while queue:
                r, c = queue.popleft()
                if visited[r][c] == 1:
                    continue
                visited[r][c] = 1

                for d in directions:
                    newR = r + d[0]
                    newC = c + d[1]
                    if newR < 0 or newC < 0:
                        pac = 1
                        continue
                    if newR == len(heights) or newC == len(heights[0]):
                        atl = 1
                        continue
                    if heights[newR][newC] <= heights[r][c]:
                        if [newR, newC] in resList:
                            return 1
                        queue.append([newR, newC])
            return pac and atl

        resList = list()
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if toOcean(i, j):
                    resList.append([i, j])
        return resList

    def pacificAtlantic_BFS_LC(self, matrix: List[List[int]]) -> List[List[int]]:
        # Check if input is empty
        if not matrix or not matrix[0]:
            return []

        num_rows, num_cols = len(matrix), len(matrix[0])

        # Setup each queue with cells adjacent to their respective ocean
        pacific_queue = collections.deque()
        atlantic_queue = collections.deque()
        for i in range(num_rows):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, num_cols - 1))
        for i in range(num_cols):
            pacific_queue.append((0, i))
            atlantic_queue.append((num_rows - 1, i))

        def bfs(queue):
            reachable = set()
            while queue:
                (row, col) = queue.popleft()
                # This cell is reachable, so mark it
                reachable.add((row, col))
                for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:  # Check all 4 directions
                    new_row, new_col = row + x, col + y
                    # Check if the new cell is within bounds
                    if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                        continue
                    # Check that the new cell hasn't already been visited
                    if (new_row, new_col) in reachable:
                        continue
                    # Check that the new cell has a higher or equal height,
                    # So that water can flow from the new cell to the old cell
                    if matrix[new_row][new_col] < matrix[row][col]:
                        continue
                    # If we've gotten this far, that means the new cell is reachable
                    queue.append((new_row, new_col))
            return reachable

        # Perform a BFS for each ocean to find all cells accessible by each ocean
        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)

        # Find all cells that can reach both oceans, and convert to list
        return list(pacific_reachable.intersection(atlantic_reachable))

if __name__ == '__main__':
    sol = Solution()
    res = sol.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
    print(res)
