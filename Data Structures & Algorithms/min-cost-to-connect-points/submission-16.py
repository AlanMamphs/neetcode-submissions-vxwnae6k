class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))
        edges.sort()
        pars = [i for i in range(n + 1)]
        sizes = [1] * (n + 1)

        def find(n):
            if pars[n] != n:
                pars[n] = find(pars[n])
            return pars[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if sizes[p1] > sizes[p2]:
                sizes[p1] += sizes[p2]
                pars[p2] = p1
            else:
                sizes[p2] += sizes[p1]
                pars[p1] = p2
            return True
        
        res = 0
        for d, i, j in edges:
            if union(i, j):
                res += d
        return res