class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        edges = defaultdict(list)
        
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges[i].append((dist, j))
                edges[j].append((dist, i))
        
        visited = set() # cycle-detection
        q = [(0, 0)] # min-heap (#dist, #index)
        res = 0
        while q:
            if len(visited) == N:
                return res
            dist, i = heapq.heappop(q)
            if i in visited:
                continue
            res += dist
            visited.add(i)

            for dist2, neighbor in edges[i]:
                if neighbor in visited:
                    continue
                heapq.heappush(q, (dist2, neighbor))

        return res