class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((t, v))
        
        q = [(0, k)]
        visited = set()
        res = 0
        while q:
            t1, u = heapq.heappop(q)
            if u in visited:
                continue
            res = t1
            visited.add(u)
            for t2, v in adj[u]:
                if v not in visited:
                    heapq.heappush(q, (t1 + t2, v))
        return res if len(visited) == n else -1