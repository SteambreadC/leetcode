from typing import Optional, List
from collections import deque, defaultdict
from sortedcontainers import SortedDict



class TimeMap:

    def __init__(self):
        self.inner = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.inner[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        ls = self.inner.get(key)
        if not ls:
            return ""
        else:
            if timestamp < ls[0][0]:
                return ""
            left, right = 0, len(ls)-1

            while left < right:
                mid = int((left+right)/2)
                if ls[mid][0] == timestamp:
                    return ls[mid][1]
                if ls[mid][0] < timestamp:
                    left = mid + 1
                elif ls[mid][0] > timestamp:
                    right = mid - 1
            return ls[right][1]

'''
class TimeMap:

    def __init__(self):
        self.inner = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.inner[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ls = self.inner.get(key)
        if not ls:
            return ""
        else:
            if timestamp < ls[0][1]:
                return ""
            for i in range(len(ls)-1, -1, -1):
                if ls[i][1] <= timestamp:
                    return ls[i][0]
'''






if __name__ == '__main__':
    obj = TimeMap()
    obj.set("key", "high", 10)
    obj.set("key", "low", 20)
    res = obj.get("key", 5)
    print(res)
    res = obj.get("key", 10)
    print(res)
    res = obj.get("key", 15)
    print(res)
    res = obj.get("key", 20)
    print(res)
