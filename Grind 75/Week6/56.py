from typing import Optional, List
from collections import deque


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Assume the list is ordered by ascending.
        start, end = 0, -1
        result = []

        intervals = sorted(intervals, key=lambda interval: interval[0])
        print(intervals)
        for i in range(len(intervals)):
            if intervals[i][0] > end:
                result.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            else:
                end = max(end, intervals[i][1])
        result.append([start, end])
        del result[0]
        return result


if __name__ == '__main__':
    sol = Solution()
    res = sol.merge([[1, 3], [8, 10], [2, 6], [15, 18]])
    print(res)
