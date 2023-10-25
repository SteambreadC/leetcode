from typing import Optional, List
from collections import deque, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s].append(s)

        return list(anagrams.values())

if __name__ == '__main__':
    sol = Solution()
    toPrint = sol.func()
    print(toPrint)
