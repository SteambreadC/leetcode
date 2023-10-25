class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sqrt = list()
        for p in points:
            s = math.sqrt(p[0]*p[0] + p[1]*p[1])
            sqrt.append(s)
        sqrt.sort()
        sq = sqrt[k-1]
        res = list()
        for p in points:
            if sq >= math.sqrt(p[0]*p[0] + p[1]*p[1]):
                res.append(p)
        return res