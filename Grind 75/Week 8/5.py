from typing import Optional, List
from collections import deque


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        longest = 0
        result = ""

        for i in range(len(s)):
            dp[i][i] = True
            if i < len(s) - 1:
                dp[i][i + 1] = (s[i] == s[i + 1])

        for j in range(2, len(s)):
            for i in range(len(s)-j):
                dp[i][i+j] = dp[i+1][i+j-1] and (s[i] == s[i+j])

        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i][j]:
                    if j-i+1 >= longest:
                        longest = j-i+1
                        result = s[i:j + 1]

        return result

    def longestPalindrome2_origin(self, s: str) -> str:
        copy = s
        result = ""
        visited = set()
        stack = deque()

        def isPalindrome(sub: str):
            rev = sub[::-1]
            return rev == sub

        stack.append(copy)
        while stack:
            q = stack.popleft()
            if q in visited:
                continue
            visited.add(q)
            if isPalindrome(q):
                result = q
                break
            else:
                stack.append(q[:-1])
                stack.append(q[1:])
        return result


if __name__ == '__main__':
    sol = Solution()
    res = sol.longestPalindrome("babad")
    print(res)
