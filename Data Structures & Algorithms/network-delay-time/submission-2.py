class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(set)

        for u, v, t in times:
            edges[u].add((v, t))
        
        q = [(0, k)]
        visited = set()
        res = 0

        while q:
            t1, u1 = heapq.heappop(q)
            if u1 in visited:
                continue
            visited.add(u1)
            res = t1
            for u2, t2 in edges[u1]:
                heapq.heappush(q, (t1+t2, u2))
        return res if len(visited) == n else -1