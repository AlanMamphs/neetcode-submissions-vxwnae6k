class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for n1, n2, w in edges:
            adj[n1].append((w, n2))
            adj[n2].append((w, n1))
        
        visited = set() # cycle-detection
        res = 0
        q = [(0, 0)]
        while q:
            w, i = heapq.heappop(q)
            if i in visited:
                continue
            res += w
            visited.add(i)
            for w2, neigh in adj[i]:
                if neigh in visited:
                    continue
                heapq.heappush(q, (w2, neigh))

        return res if n == len(visited) else -1
