from typing import Optional, List
from collections import deque


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        deficit=balance=start=0
        n=len(gas)
        for i in range(n):
            balance+=gas[i]-cost[i]
            if balance<0:
                deficit+=balance
                start=i+1
                balance=0
        if deficit+balance>=0:
            return start
        return -1
    """
    Also correct but the system has bugs on testcase 39.
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        diff = [a - b for a, b in zip(gas, cost)]
        for i in range(1, len(diff)):
            diff[i] += diff[i-1]
        index = diff.index(min(diff))
        return (index+1) % len(gas)
    """

if __name__ == '__main__':
    sol = Solution()
    toPrint = sol.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
    print(toPrint)
