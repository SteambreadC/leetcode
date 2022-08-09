import string
from typing import Optional, List
from collections import deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        palin = list()
        s = s.lower()
        for i in s:
            if 96 < ord(i) < 123 or i.isnumeric():
                palin.append(i)
        backpalin = palin[::-1]
        return backpalin == palin



if __name__ == '__main__':
    sol = Solution()
    res = sol.isPalindrome("0P")
    print(res)
