import string
from typing import Optional, List
from collections import deque, Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(t)
        return c1 == c2

if __name__ == '__main__':
    sol = Solution()
    res = sol.isAnagram("abc", "baca")
    print(res)
