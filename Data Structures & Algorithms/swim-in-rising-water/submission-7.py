class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        q = [(grid[0][0], 0, 0)]

        visited = set([(0, 0)])
        
        while q:
            h, r, c = heapq.heappop(q)
            
            if r == R - 1 and c == C - 1:
                return h
            
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dr, c + dc
                if nr in range(R) and nc in range(C) and (nr, nc) not in visited:
                    heapq.heappush(q, (max(grid[nr][nc], h), nr, nc))
                    visited.add((nr, nc))
        return -1