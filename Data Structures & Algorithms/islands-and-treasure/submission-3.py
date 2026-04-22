class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        R = len(grid)
        C = len(grid[0])
        q = deque()
        visited = set()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
                    visited.add((r, c))
        
        while q:
            for _ in range(len(q)):
                r,c,i = q.popleft()
                
                grid[r][c] = i
                for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                    r2 = r+dr
                    c2 = c+dc
                    if r2 not in range(R) or c2 not in range(C) or (r2, c2) in visited or grid[r2][c2] == -1:
                        continue
                    visited.add((r2, c2))
                    q.append((r2, c2, i+1))
            





