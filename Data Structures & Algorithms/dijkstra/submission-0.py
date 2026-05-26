class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
        
        visit = {i: -1 for i in range(n)}
        q = [(0, src)]
        while q:
    
            w1, u = heapq.heappop(q)
            if visit[u] != -1:
                continue
            visit[u] = w1
            
            for v, w2 in adj[u]:
                if visit[v] == -1:
                    heapq.heappush(q, (w1 + w2, v))
    
        return visit

            
        