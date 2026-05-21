class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(set)

        for u, v, t in times:
            edges[u].add((t, v))
        
        visited = set()
        res = 0
        q = [(0, k)]

        while q:
            t1, n1 = heapq.heappop(q)
            if n1 in visited:
                continue
            visited.add(n1)
            
            res = t1
            for t2, n2 in edges[n1]:
                # if n2 in visited:
                #     continue
                
                heapq.heappush(q, (t1 + t2, n2))
        
        return res if len(visited) == n else -1