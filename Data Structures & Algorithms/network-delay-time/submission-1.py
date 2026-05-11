class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        q = [(0, k)]
        visited = set()
        t = 0
        while q:
            w1, v1 = heapq.heappop(q)
            if v1 in visited:
                continue
            t = w1
            visited.add(v1)
            for v2, w2 in edges[v1]:
                heapq.heappush(q, (w2+w1, v2))
        return t if len(visited) == n else -1


