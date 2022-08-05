from typing import Optional, List
import collections


class MyQueue:

    def __init__(self):
        self.stackIn=collections.deque()
        self.stackOut=collections.deque()

    def push(self, x: int) -> None:
        self.stackIn.append(x)

    def pop(self) -> int:
        if not self.stackOut:
            while self.stackIn:
                p = self.stackIn.pop()
                self.stackOut.append(p)
        return self.stackOut.pop()

    def peek(self) -> int:
        if not self.stackOut:
            while self.stackIn:
                p = self.stackIn.pop()
                self.stackOut.append(p)
        return self.stackOut[-1]

    def empty(self) -> bool:
        if len(self.stackIn) + len(self.stackOut) <= 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
