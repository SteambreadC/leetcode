from typing import Optional, List
from collections import deque

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i, j = 0, 0
        d = directions[0]
        visited = set()
        visited.add((i,j))
        result = [matrix[i][j]]
        tag = 0

        def changeDirections(d):
            nonlocal directions
            i = directions.index(d)
            return directions[(i+1)%4]

        while 0<=i<len(matrix) and 0<=j<len(matrix[0]) and tag < 2:
            newi = i + d[0]
            newj = j + d[1]
            if 0 <= newi <len(matrix) and 0 <= newj <len(matrix[0]) and (newi, newj) not in visited:
                    i = newi
                    j = newj
                    visited.add((newi,newj))
                    tag = 0
                    result.append(matrix[i][j])
            else:
                d = changeDirections(d)
                tag += 1
        return result





if __name__ == '__main__':
    sol = Solution()
    res = sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]
)
    print(res)
