class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        q = deque()
        R = len(grid)
        C = len(grid[0])
        fresh = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    visited.add((r, c))
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        if not count:
            return 0
        res = 0
        while fresh and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    r2 = r + dr
                    c2 = c + dc
                    if r2 in range(R) and c2 in range(C) and (r2, c2) not in visited and grid[r2][c2] == 1:
                        q.append((r2, c2))
                        visited.add((r2, c2))
                        fresh -= 1

            res += 1
        

        return res if not fresh else -1