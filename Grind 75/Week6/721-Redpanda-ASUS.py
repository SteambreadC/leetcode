from typing import Optional, List
from collections import deque


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        nodes = {}
        resultList = []

        id = -1
        for addresses in accounts:
            for addr in addresses[1:]:
                if addr not in nodes.keys():
                    nodes[addr] = []
                nodes[addr].extend(addresses[1:])
                nodes[addr].remove(addr)

        group = set()
        visited = set()

        def DFS(addr):
            nonlocal nodes
            if addr not in group:
                group.add(addr)
                for ad in nodes[addr]:
                    DFS(ad)
            return

        for addr in nodes.keys():
            if addr in visited:
                continue
            DFS(addr)
            visited.update(group)
            for addresses in accounts:
                if addr in addresses:
                    user = addresses[0]
            res = []
            res.extend(group)
            res.sort()
            res.insert(0,user)
            resultList.append(res)
            group.clear()

        return resultList


if __name__ == '__main__':
    sol = Solution()
    res = sol.accountsMerge(
        [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"],
         ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]])
    print(res)
