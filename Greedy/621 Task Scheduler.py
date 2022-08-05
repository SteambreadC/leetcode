import collections
from typing import Optional, List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        taskCounter = [0] * 26
        for t in tasks:
            taskCounter[ord(t) - ord('A')] += 1
        taskCounter=sorted(taskCounter,reverse=True)
        maxRunning = max(taskCounter)
        maxN = taskCounter.count(maxRunning)
        res = (maxRunning-1) * (n+1) + maxN
        return max(res, len(tasks))


if __name__ == '__main__':
    sol = Solution()
    res = sol.leastInterval(["A", "A", "A", "B", "B", "B", "B", "C"], n=2)
    print(res)
