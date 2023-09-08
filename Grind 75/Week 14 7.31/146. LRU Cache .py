from typing import Optional, List
from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.queue = deque()
        self.cap = capacity

    def get(self, key: int) -> int:
        res = self.map.get(key, -1)
        if res is not -1:
            t = self.map.pop(key)
            self.map[key] = t
        return res

    def put(self, key: int, value: int) -> None:
        oldVal = self.map.get(key, -1)
        self.map[key] = value
        if oldVal == -1:
            if self.cap:
                self.cap -= 1
            else:
                self.map.pop(next(iter(self.map)))
        else:
            self.map.pop(key)
        self.map[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    sol = Solution()
    res = sol.longestPalindrome(["lc", "cl", "gg"])
    print(res)
