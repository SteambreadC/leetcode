from typing import Optional, List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = 0
        pos = [0, 0]
        visited = [row[:] for row in matrix] # Or use deep copy. 只有deep copy可以copy多维数组
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                visited[i][j] = 0
        size = len(matrix[0]) * len(matrix)
        res = list()

        while len(res) < size:
            while direction == 0:
                if -1<pos[0]<len(matrix) and -1<pos[1]<len(matrix[0]) and visited[pos[0]][pos[1]] == 0:
                    res.append(matrix[pos[0]][pos[1]])
                    visited[pos[0]][pos[1]] = 1
                    pos[1] += 1
                else:
                    pos[1] -= 1
                    pos[0] += 1
                    direction += 1
            while direction == 1:
                if -1<pos[0]<len(matrix) and -1<pos[1]<len(matrix[0]) and visited[pos[0]][pos[1]] == 0:
                    res.append(matrix[pos[0]][pos[1]])
                    visited[pos[0]][pos[1]] = 1
                    pos[0] += 1
                else:
                    pos[0] -= 1
                    pos[1] -= 1
                    direction += 1
            while direction == 2:
                if -1<pos[0]<len(matrix) and -1<pos[1]<len(matrix[0]) and visited[pos[0]][pos[1]] == 0:
                    res.append(matrix[pos[0]][pos[1]])
                    visited[pos[0]][pos[1]] = 1
                    pos[1] -= 1
                else:
                    pos[1] += 1
                    pos[0] -= 1
                    direction += 1
            while direction == 3:
                if -1<pos[0]<len(matrix) and -1<pos[1]<len(matrix[0]) and visited[pos[0]][pos[1]] == 0:
                    res.append(matrix[pos[0]][pos[1]])
                    visited[pos[0]][pos[1]] = 1
                    pos[0] -= 1
                else:
                    pos[0] += 1
                    pos[1] += 1
                    direction = 0

        return res

    def spiralOrder_LC(self, matrix: List[List[int]]) -> List[int]:
        VISITED = 101
        rows, columns = len(matrix), len(matrix[0])
        # Four directions that we will move: right, down, left, up.
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Initial direction: moving right.
        current_direction = 0
        # The number of times we change the direction.
        change_direction = 0
        # Current place that we are at is (row, col).
        # row is the row index; col is the column index.
        row = col = 0
        # Store the first element and mark it as visited.
        result = [matrix[0][0]]
        matrix[0][0] = VISITED

        while change_direction < 2:

            while True:
                # Calculate the next place that we will move to.
                next_row = row + directions[current_direction][0]
                next_col = col + directions[current_direction][1]

                # Break if the next step is out of bounds.
                if not (0 <= next_row < rows and 0 <= next_col < columns):
                    break
                # Break if the next step is on a visited cell.
                if matrix[next_row][next_col] == VISITED:
                    break

                # Reset this to 0 since we did not break and change the direction.
                change_direction = 0
                # Update our current position to the next step.
                row, col = next_row, next_col
                result.append(matrix[row][col])
                matrix[row][col] = VISITED

            # Change our direction.
            current_direction = (current_direction + 1) % 4
            # Increment change_direction because we changed our direction.
            change_direction += 1


if __name__ == '__main__':
    sol=Solution()
    print(sol.spiralOrder(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))