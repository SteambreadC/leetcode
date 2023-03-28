from collections import deque
from typing import Optional, List
import operator


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }
        stack = deque()
        for token in tokens:
            if token.lstrip('-').isdigit():
                stack.append(int(token))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                n = int(ops[token](int(n1), int(n2)))
                stack.append(n)
        return stack[0]


