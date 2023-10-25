from typing import Optional, List
from collections import deque


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return

        mydict = {}
        res = []
        temp = []
        isnull = 1
        mydict[2] = ['a','b','c']
        mydict[3] = ['d','e','f']
        mydict[4] = ['g','h','i']
        mydict[5] = "jkl"
        mydict[6] = "mno"
        mydict[7] = "pqrs"
        mydict[8] = "tuv"
        mydict[9] = "wxyz"

        for d in digits:
            for c in mydict[int(d)]:
                if isnull == 1:
                    res.append(c)
                else:
                    for l in res:
                        temp.append(l+c)

            if isnull == 0:
                res = temp.copy()
                temp.clear()
            isnull = 0
        return res


if __name__ == '__main__':
    sol = Solution()
    res = sol.longestPalindrome(["lc", "cl", "gg"])
    print(res)
