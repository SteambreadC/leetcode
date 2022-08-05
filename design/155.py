from typing import Optional, List
from collections import deque

class MinStack:

    def __init__(self):
        self.storageStack = deque()
        self.helpStack = deque()

    def push(self, val: int) -> None:
        self.storageStack.append(val)
        if self.helpStack:
            self.helpStack.append(min(self.helpStack[-1], val))
        else:
            self.helpStack.append(val)

    def pop(self) -> None:
        self.storageStack.pop()
        self.helpStack.pop()

    def top(self) -> int:
        return self.storageStack[-1]

    def getMin(self) -> int:
        return self.helpStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()