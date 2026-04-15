class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        res = 0

        def dfs(r, c):
            if r not in range(R) or c not in range(C) or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            up = dfs(r + 1, c)
            down = dfs(r - 1, c)

            return 1 + left + right + up + down

        for r in range(R):
            for c in range(C):
                res = max(res, dfs(r, c))

        return res


