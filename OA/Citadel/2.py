from typing import Optional, List
from collections import deque


def getMaxSubarrayLen(team_a, team_b):
    n = len(team_a)
    max_len = 0
    i = 0
    j = 0

    while i < n and j < n:
        if team_b[j] >= team_a[i]:
            # Extend the subarray in team b
            j += 1
        else:
            # Move to the next hacker in team a
            i += 1

        # Update the maximum lengthmax
        max_len = max(max_len, (j - i))

    return max_len


if __name__ == '__main__':
    res = getMaxSubarrayLen([5, 2, 4, 2], [3, 6, 2, 1])
    print(res)
