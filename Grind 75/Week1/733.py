import string
from typing import Optional, List
from collections import deque, Counter


class Solution:
    def floodFill_BFS(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        stack = deque()
        stack.append([sr,sc])
        origin = image[sr][sc]
        image[sr][sc] = color
        if origin == color:
            return image
        while stack:
            q = stack.popleft()
            row, col = q[0], q[1]
            for direc in directions:
                newR = row + direc[0]
                newC = col + direc[1]
                if -1<newR<len(image) and -1<newC <len(image[0]):
                    if image[newR][newC] == origin:
                        image[newR][newC] = color
                        stack.append([newR,newC])
        return image

    def floodFill_DFS(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        origin = image[sr][sc]
        if origin == color:
            return image

        def dfs(r, c):
            if image[r][c] == origin:
                image[r][c] = color
                for d in directions:
                    newR, newC = r + d[0], c + d[1]
                    if -1 < newR < len(image) and -1 < newC < len(image[0]):
                        dfs(newR, newC)

        dfs(sr, sc)
        return image


if __name__ == '__main__':
    sol = Solution()
    res = sol.isAnagram("abc", "baca")
    print(res)
