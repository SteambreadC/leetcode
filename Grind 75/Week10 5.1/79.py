from typing import Optional, List
from collections import deque


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def backtrack(position, index):
            nonlocal word, directions
            if index == len(word):
                return True
            I, J = position[0], position[1]
            if I < 0 or I >= m or J < 0 or J >= n or visited[i][j] or board[i][j] != word[index]:
                return False
            visited[i][j] = True
            for d in directions:
                NI, NJ = I + d[0], J + d[1]
                if backtrack((NI, NJ), index + 1):
                    return True
            visited[I][J] = False
            return False

        for i in range(m):
            for j in range(n):
                    if backtrack((i, j), 0):
                        return True

        return False


if __name__ == '__main__':
    sol = Solution()
    res = sol.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED")
    print(res)
