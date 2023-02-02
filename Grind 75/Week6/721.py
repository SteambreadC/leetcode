from typing import Optional, List
from collections import deque


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        hashmap = {}
        groups = {}
        resultMap = {}
        id = -1

        for item in accounts:
            name = item[0]
            addr = item[1:]
            if name not in hashmap:
                hashmap[name] = []
            hashmap[name].append(addr)
        for it in hashmap.items():
            name = it[0]
            addrs = it[1]
            id += 1
            tag = id
            for addr in addrs:
                if groups.get(addr):
                    tag = groups[addr]
            for addr in addrs:
                groups[addr] = tag



        # print(hashmap)


if __name__ == '__main__':
    sol = Solution()
    res = sol.accountsMerge(
        [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"],
         ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]])
    print(res)
