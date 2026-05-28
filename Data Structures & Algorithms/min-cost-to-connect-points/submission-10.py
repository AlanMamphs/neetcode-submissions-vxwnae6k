class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        q = [(0, 0)]
        visited = set()
        res = 0
        while q:
            d1, i = heapq.heappop(q)
            if i in visited:
                continue
            res += d1
            visited.add(i)
            for d2, j in adj[i]:
                if j not in visited:
                    heapq.heappush(q, (d2, j))
        return res

        