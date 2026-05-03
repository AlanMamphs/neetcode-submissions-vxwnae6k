class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R = len(grid)
        C = len(grid[0])
        q = []
        visited = set()
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    continue
                q.append((r, c, 0))
                visited.add((r, c))
        while q:
            temp = []
            for r, c, d in q:
                grid[r][c] = d
                for dr, dc in ((1, 0), (-1, 0), (0, -1), (0, 1)):
                    r2, c2 = r+dr, c+dc
                    if r2 not in range(R) or c2 not in range(C) or (r2, c2) in visited or grid[r2][c2] == -1:
                        continue
                    
                    visited.add((r2, c2))
                    temp.append((r2, c2, d+1))
            
            q = temp
        





