class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars = [0] * 128
        res = 0
        for c in s:
            chars[ord(c)] += 1
            if chars[ord(c)] >= 2:
                chars[ord(c)] -= 2
                res += 2

        # for i in range(len(chars)):
        #    if chars[i]>=1:
        #        res+=1
        #        break
        if res < len(s):
            res += 1

        return res
