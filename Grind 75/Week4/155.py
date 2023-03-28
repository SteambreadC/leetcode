from typing import Optional, List
from collections import deque


class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min or val <= self.min[-1]:
            self.min.append(val)

    def pop(self) -> None:
        temp = self.top()
        if temp == self.min[-1]:
            self.min.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]



if __name__ == '__main__':
    s = MinStack()
    s.push(512)
    s.push(-1024)
    s.push(-1024)
    s.push(512)
    s.pop()
    print(s.getMin())
    s.pop()
    print(s.getMin())
    s.pop()
    print(s.getMin())
