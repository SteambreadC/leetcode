from typing import Optional, List
from collections import deque


class Solution:
    def myAtoi(self, s: str) -> int:
        posTag = 1
        i = 0
        minI, maxI = -pow(2,31), pow(2, 31) - 1
        result = ""
        if not s:
            return 0

        while i < len(s) and s[i] == " ":
            i += 1
        if i < len(s) and s[i] == "-":
            posTag = -1
            i += 1
        elif i < len(s) and s[i] == "+":
            i += 1
        while i < len(s) and ord("0") <= ord(s[i]) <= ord("9"):
            result += s[i]
            i += 1

        if not result:
            return 0
        r = int(result) * posTag
        r = max(r, minI)
        r = min(r, maxI)
        return r


if __name__ == '__main__':
    sol = Solution()
    res = sol.myAtoi(" ")
    print(res)
