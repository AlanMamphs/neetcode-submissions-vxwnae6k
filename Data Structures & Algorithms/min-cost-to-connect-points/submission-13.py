class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        q = []
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(q, (dist, i, j))
        
        pars = list(range(n + 1))
        size = [1] * (n + 1)

        def find(n):
            if n != pars[n]:
                pars[n] = find(pars[n])
            return pars[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if size[p1] > size[p2]:
                size[p1] += size[p2]
                pars[p2] = p1
            else:
                size[p2] += size[p1]
                pars[p1] = p2
            return True
        
        res = 0
        while q:
            dist, u, v = heapq.heappop(q)
            if union(u, v):
                res += dist
        return res
