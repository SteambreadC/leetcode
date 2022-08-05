from typing import Optional, List
import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # courses[2i] means course i need courses in this list to be taken.
        # courses[2i+1] means if someone takes course i, he can now take courses in this list.
        courses = [[] for i in range(numCourses * 2)]
        taken = list()
        preL = -1

        for cp in prerequisites:
            courses[cp[1] * 2 + 1].append(cp[0])
            courses[cp[0] * 2].append(cp[1])
        while len(taken) < numCourses:
            if preL == len(taken):
                return []
            preL = len(taken)
            for j in range(0, len(courses), 2):
                if not courses[j]:
                    taken.append(int(j / 2))
                    for i in courses[j + 1]:
                        courses[2 * i].remove(int(j / 2))
                    courses[j] = -1
                    courses[j + 1] = -1
        return taken

    def findOrder_indegree(self, numCourses, prerequisites):
        # 和我的方法一样，使用了队列
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # Prepare the graph
        adj_list = collections.defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)

            # Record each node's in-degree
            indegree[dest] = indegree.get(dest, 0) + 1

        # Queue for maintainig list of nodes that have 0 in-degree
        zero_indegree_queue = collections.deque([k for k in range(numCourses) if k not in indegree])

        topological_sorted_order = []

        # Until there are nodes in the Q
        while zero_indegree_queue:

            # Pop one node with 0 in-degree
            vertex = zero_indegree_queue.popleft()
            topological_sorted_order.append(vertex)

            # Reduce in-degree for all the neighbors
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1

                    # Add neighbor to Q if in-degree becomes 0
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)

        return topological_sorted_order if len(topological_sorted_order) == numCourses else []


if __name__ == '__main__':
    sol = Solution()
    res = sol.findOrder(2, [[1, 0]])
    print(res)
