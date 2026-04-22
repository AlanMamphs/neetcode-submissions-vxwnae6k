class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        visited = set()
        def dfs(r, c):
            if r not in range(R) or c not in range(C) or (r,c) in visited or grid[r][c] == 0:
                return 0
            visited.add((r, c))
            res = 1
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                res += dfs(r+dr, c+dc)
            return res
        res = 0
        for r in range(R):
            for c in range(C):
                res = max(res, dfs(r, c))

        return res


