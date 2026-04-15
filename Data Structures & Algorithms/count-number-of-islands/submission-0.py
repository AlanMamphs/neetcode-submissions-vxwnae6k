class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        islands = 0

        def dfs(r, c):
            if r not in range(R) or c not in range(C) or grid[r][c] == '0':
                return 0
            grid[r][c] = '0'
            for dir in directions:
                dfs(r + dir[0], c + dir[1])


        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1

        return islands
            
