from typing import Optional, List
from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack_index = []
        stack_val = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(len(stack_val)-1, -1, -1):
                if stack_val[j] < temperatures[i]:
                    stack_val.pop()
                    idx = stack_index.pop()
                    res[idx] = i - idx
                else:
                    break
            stack_index.append(i)
            stack_val.append(temperatures[i])
        return res


if __name__ == '__main__':
    sol = Solution()
    toPrint = sol.func()
    print(toPrint)
