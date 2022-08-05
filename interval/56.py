from typing import Optional, List
from collections import deque


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # double check what the problem want first!
        i, j = 0, 0
        l = len(intervals)
        intervals.sort(key=lambda x: x[0])
        while i < l - 1:
            j = i + 1
            left, right = intervals[i][0], intervals[i][1]
            while j < l and right >= intervals[j][0]:
                right = max(right, intervals[j][1])
                j += 1
            if j > i + 1:
                del intervals[i:j]
                intervals.insert(i, [left, right])
                i += 1
                l = l - j + i
            else:
                i = j
        return intervals


if __name__ == "__main__":
    sol = Solution()
    res = sol.merge([[1, 5], [4,8], [9,10], [0,1]])
    print(res)
