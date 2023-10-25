from typing import Optional, List
from collections import deque

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        zeros = [0] * 10
        count1 = zeros.copy()
        count2 = zeros.copy()
        count3 = zeros.copy()

        for i in range(0, 9):
            for j in range(0, 9):
                num = board[i][j]
                if num.isdigit():
                    count1[int(num)] += 1
                num2 = board[j][i]
                if num2.isdigit():
                    count2[int(num2)] += 1
            if max(count1) > 1 or max(count2) > 1:
                return False
            else:
                count1 = zeros.copy()
                count2 = zeros.copy()
        for i in range(0, 3):
            for j in range(0, 3):
                for part in board[3 * i:3 * i + 3]:
                    for n in part[3 * j:3 * j + 3]:
                        if n.isdigit():
                            count3[int(n)] += 1
                if max(count3) > 1:
                    return False
                else:
                    count3 = zeros.copy()
        return True



if __name__ == '__main__':
    sol = Solution()
    toPrint = sol.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
    print(toPrint)
