class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        q = [(grid[0][0], 0, 0)]

        visited = set([0, 0])
        res = 0
        while q:
            h, r, c = heapq.heappop(q)
            res = max(res, grid[r][c])
            if (r, c) == (R-1, C-1):
                return res
        

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r+dr, c+dc
                if nr in range(R) and nc in range(C) and (nr, nc) not in visited:
                    nh = max(h, grid[nr][nc])
                    heapq.heappush(q, (nh, nr, nc))
                    visited.add((nr, nc))


