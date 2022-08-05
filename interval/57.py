from typing import Optional, List
from collections import deque


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        left, right = newInterval[0], newInterval[1]
        newL, newR = 0, len(intervals) - 1
        for index, i in enumerate(intervals):
            if i[1] < left:
                newL = index + 1
            if i[0] > right:
                newR = index - 1
                break
        if newL <= newR:
            newInterval[0] = min(intervals[newL][0], left)
            newInterval[1] = max(intervals[newR][1], right)
            del intervals[newL:newR+1]

        intervals.insert(newL, newInterval)
        return intervals


if __name__ == "__main__":
    sol = Solution()
    res = sol.insert([[1, 5]], [6, 8])
    print(res)
