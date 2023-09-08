from typing import Optional, List
from collections import deque


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        def Search(i: int, j: int, p=0):
            nonlocal board, word
            res = 0
            if board[i][j] is not word[p] or visited[i][j]:
                return False
            if p == (len(word) - 1) and board[i][j] == word[p]:
                return True
            else:
                visited[i][j] = True
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                    res += Search(ni, nj, p + 1)
                    visited[i][j] = False
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if Search(i, j):
                        return True
        return False


if __name__ == '__main__':
    sol = Solution()
    res = sol.exist([["a", "a", "a", "a"], ["a", "a", "a", "a"], ["a", "a", "a", "a"]], "aaaaaaaaaaaaa")
    print(res)
