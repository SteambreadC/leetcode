from queue import Queue
from typing import Optional, List
import collections


class Solution:
    def numBusesToDestination_deque(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        reachable = collections.deque()
        reachable.append(source)
        reachable.append(-1)
        visited = [0] * len(routes)
        bus = 0

        while reachable:
            station = reachable.popleft()
            if station == -1:
                bus += 1
            for index, route in enumerate(routes):
                if visited[index] == 1:
                    continue
                if station in route:
                    visited[index] = 1
                    for nextStation in route:
                        if nextStation == target:
                            return bus + 1
                        if nextStation != station:
                            reachable.append(nextStation)
                    reachable.append(-1)

        return -1

    def numBusesToDestination_BFS1(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        allCount = 501
        routes = list(map(set, routes))
        graph = dict()
        source_bus = []
        target_bus = set()
        for i in range(len(routes)):
            graph[i] = set()
            if source in routes[i]:
                source_bus.append(i)
            if target in routes[i]:
                target_bus.add(i)

        for i, route in enumerate(routes):
            for j in range(i + 1, len(routes)):
                for station in routes[i]:
                    if station in routes[j]:
                        graph[i].add(j)
                        graph[j].add(i)

        for s_bus in source_bus:
            count = 1
            neighbor = collections.deque()
            neighbor.append(s_bus)
            visited = [0] * len(routes)
            if s_bus in target_bus:
                return count
            while neighbor:
                bus = neighbor.popleft()
                visited[bus] = 1
                count += 1
                for b in graph[bus]:
                    if b in target_bus:
                        allCount = min(allCount, count)
                    if visited[b] == 0:
                        neighbor.append(b)
        return allCount if allCount <= 500 else -1

    def numBusesToDestination_BFSUseBothStopsAndBus(self, routes: List[List[int]], source: int, target: int) -> int:
        stops = collections.defaultdict(list)
        for bus, route in enumerate(routes):
            for stop in route:
                stops[stop].append(bus)

        if source not in stops or target not in stops:
            return -1

        q = collections.deque([source])
        visited = set([source])
        busCounts = 0
        while q:
            sameLevelCounts = len(q)
            for _ in range(sameLevelCounts):
                current = q.popleft()
                if current == target:
                    return busCounts
                for bus in stops[current]:
                    for stop in routes[bus]:
                        if stop not in visited:
                            visited.add(stop)
                            q.append(stop)
                    routes[bus] = []  # set visited route to empty
            busCounts += 1
        return -1


if __name__ == '__main__':
    sol = Solution()
    res = sol.findOrder(2, [[1, 0]])
    print(res)
