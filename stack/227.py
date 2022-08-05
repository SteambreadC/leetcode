from typing import Optional, List
from collections import deque
import operator


class Solution:
    def calculate(self, s: str) -> int:
        def cal(i=0):
            nonlocal stack
            b = stack.pop()
            op = stack.pop()
            a = stack.pop()
            if i==0:
                res = int(ops[op](int(a), int(b)))
            else:
                res = int(ops[op](int(b), int(a)))
            stack.append(res)
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }

        stack = deque()
        number = str()
        for c in s:
            if c == " ":
                continue
            if c in ops:
                stack.append(int(number))
                number = str()
                if len(stack) > 1 and stack[-2] in ('/', '*'):
                    cal()
                stack.append(c)
            else:
                number += c
        stack.append(int(number))
        if len(stack) > 1 and stack[-2] in ('/', '*'):
            cal()
        stack.reverse()
        while len(stack) >= 3:
            cal(1)
        return stack[0]


if __name__ == '__main__':
    sol = Solution()
    toPrint = sol.calculate("1*2+6/3+5*2-5")
    print(toPrint)
