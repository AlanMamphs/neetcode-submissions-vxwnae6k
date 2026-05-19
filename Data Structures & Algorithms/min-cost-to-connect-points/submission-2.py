class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = defaultdict(set)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges[i].add((dist, j))
                edges[j].add((dist, i))
        
        q = [(0, 0)]
        visited = set()
        res = 0
        while q:
            if len(visited) == len(points):
                return res
            dist, i = heapq.heappop(q)
            if i in visited:
                continue
            res += dist
            visited.add(i)
            for dist2, j in edges[i]:
                if j in visited:
                    continue
                heapq.heappush(q, (dist2, j))
        return res
