class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                edges[i].append((dist, j))
                edges[j].append((dist, i))
        
        q = [(0, 0)]
        visited = set()
        res = 0

        
        while q:
            d1, p1 = heapq.heappop(q)
            if p1 in visited:
                continue
            
            visited.add(p1)
            res += d1
            if len(visited) == n:
                return res
            for d2, p2 in edges[p1]:
                if p2 in visited:
                    continue
                heapq.heappush(q, (d2, p2))
        
        return -1
                


