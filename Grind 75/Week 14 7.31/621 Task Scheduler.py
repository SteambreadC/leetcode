from typing import Optional, List
from collections import deque, defaultdict


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ''' We should find 2 possible min values:
         1. the total number of tasks: taskCount
         2. the min time needed when adding cooldown with the most common tasks
         (There could be several most common tasks): cdTime
         The bigger value will be our answer.
         '''
        taskCount, cdTime =len(tasks), 0
        hashMap = dict()
        maxCount = 0
        for t in tasks:
            hashMap[t] = hashMap.get(t,0) + 1
            maxCount = max(maxCount, hashMap[t])
        # commonVals = [val for val, count in hashMap.items() if count == maxCount]
        commonVals = sum(1 for count in hashMap.values() if count == maxCount)

        cdTime = (n+1) * maxCount - n + commonVals -1
        return max(taskCount,cdTime)




if __name__ == '__main__':
    sol = Solution()
    res = sol.leastInterval(["A","A","A","B","B","B"], 2)
    print(res)
