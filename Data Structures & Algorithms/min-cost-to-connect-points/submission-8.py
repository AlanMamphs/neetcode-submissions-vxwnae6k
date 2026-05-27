class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minH = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                heapq.heappush(minH, (dist, i, j))
        
        pars = [i for i in range(len(minH) + 1)]
        rank = [1 for i in range(len(minH) + 1)]

        def find(n):
            if n != pars[n]:
                pars[n] = find(pars[n])
            return pars[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                pars[p2] = p1
                rank[p1] += rank[p2]
            else:
                pars[p1] = p2
                rank[p2] += rank[p1]
            return True
        res = 0
        while minH:
            d, u, v = heapq.heappop(minH)
            if union(u, v):
                res += d
        return res

            