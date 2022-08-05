from typing import Optional, List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lenRow = len(matrix[0])
        lenCol = len(matrix)
        left, right = 0, lenCol - 1

        while left <= right:
            mid = int((right + left) / 2)
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            if matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1

        targetRow = matrix[mid]
        left, right = 0, lenRow - 1
        while left < right:
            mid = int((right + left) / 2)
            if targetRow[mid] == target:
                return True
            if targetRow[mid] > target:
                right = mid
            else:
                left = mid + 1
        return targetRow[right] == target

