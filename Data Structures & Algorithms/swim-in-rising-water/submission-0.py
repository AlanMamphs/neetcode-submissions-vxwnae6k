class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        visited = set([(0, 0)])
        q = [(grid[0][0], 0, 0)]
        while q:
            w1, r1, c1 = heapq.heappop(q)
            if r1 == R - 1 and c1 == C - 1:
                return w1
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                r2 = r1 + dr
                c2 = c1 + dc
                if r2 not in range(R) or c2 not in range(C) or (r2, c2) in visited:
                    continue
                visited.add((r2, c2))
                heapq.heappush(q, (max(w1, grid[r2][c2]), r2, c2))