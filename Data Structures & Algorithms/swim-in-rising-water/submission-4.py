class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        visited = set([(0, 0)])
        q = [(grid[0][0], 0, 0)]

        while q:
            t, r1, c1 = heapq.heappop(q)
            if r1 == (R - 1) and c1 == (C - 1):
                return t
            visited.add((r1, c1))
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                r2, c2 = r1 + dr, c1 + dc

                if r2 in range(R) and c2 in range(C) and (r2, c2) not in visited:
                    heapq.heappush(q, (max(t, grid[r2][c2]), r2, c2))
                    visited.add((r2, c2))