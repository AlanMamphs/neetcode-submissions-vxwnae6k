

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodes = defaultdict(list)

        for u, v, t in times:
            nodes[u].append((t, v))
        
        q = [(0, k)]

        res = 0
        visited = set()

        while q:
            t, n1 = heapq.heappop(q)
            if n1 in visited:
                continue
            res = t
            visited.add(n1)
            if len(visited) == n:
                return res
            for t2, n2 in nodes[n1]:
                if n2 not in visited:
                    heapq.heappush(q, (t + t2, n2))
        return -1