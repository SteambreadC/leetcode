from typing import Optional, List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = list()
        preSize = 200

        for i in strs:
            if len(i) <= preSize:
                preSize = len(i)

        for i in range(preSize):
            prefix.append(strs[0][i])
            for string in strs:
                if string[i] != prefix[i]:
                    prefix.pop()
                    res = ''.join(prefix)
                    return res

        res = ''.join(prefix)
        return res