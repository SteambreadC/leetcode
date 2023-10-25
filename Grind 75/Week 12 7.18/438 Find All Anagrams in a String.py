from typing import Optional, List
from collections import deque, defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic = defaultdict(int)
        comp = defaultdict(int)
        tag = True
        res = []
        for c in p:
            dic[c] += 1
        for c in s[0:len(p)]:
            comp[c] += 1
        if all(comp[k] == dic[k] for k in dic.keys()):
            res.append(0)

        for i in range(1, len(s)-len(p)+1):
            a = s[i+len(p)-1]
            b = s[i-1]
            comp[b] -= 1
            comp[a] += 1
            if all(comp[k] == dic[k] for k in dic.keys()):
                res.append(i)
        return res





if __name__ == '__main__':
    sol = Solution()
    res = sol.findAnagrams("cabebabacd","abc")
    print(res)
