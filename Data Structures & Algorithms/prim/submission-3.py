class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u, v, w in edges:
            adj[u].append((w, v))
            adj[v].append((w, u))

        res = 0
        visited = set()

        q = [(0, edges[0][0])]

        while q:
            w1, n1 = heapq.heappop(q)
            if n1 in visited:
                continue
            res += w1
            visited.add(n1)

            for w2, n2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(q, (w2, n2))
        return res if len(visited) == n else -1