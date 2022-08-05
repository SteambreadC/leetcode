from typing import Optional, List
import collections
import copy


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return ""
        countS = [0] * 58
        countT = copy.copy(countS)
        countNew = copy.copy(countS)
        for char in s:
            countS[ord(char) - 65] += 1
        for char in t:
            countT[ord(char) - 65] += 1
        for i in range(n):
            countNew[ord(s[i]) - 65] += 1
        for i in range(58):
            countNew[i] -= countT[i]
        left, right, size = 0, n - 1, m + 1
        res = []
        while left < m:
            tag = min(countNew)
            if tag < 0:
                if right == m-1:
                    break
                right += 1
                countNew[ord(s[right])-65] += 1
                continue
            else:
                if tag == 0:
                    if right-left+1 <= size:
                        size = right - left + 1
                        res = s[left:right + 1]
                countNew[ord(s[left])-65] -= 1
                left += 1
        return res if size <= m else ""


if __name__ == '__main__':
    sol = Solution()
    res = sol.minWindow("cabwefgewcwaefgcf", "cae")
    print(res)
