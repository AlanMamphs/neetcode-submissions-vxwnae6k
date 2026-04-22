class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        C = len(grid[0])
        R = len(grid)
        def dfs(r, c):
            if r not in range(R) or c not in range(C) or (r, c) in visited or grid[r][c] == '0':
                return False
            
            visited.add((r, c))

            for dr, dc in ((1,0), (0,1), (-1, 0), (0, -1)):
                dfs(r + dr, c + dc)
        
            return True
        res = 0
        for r in range(R):
            for c in range(C):
                if dfs(r, c):
                    res += 1
        return res





