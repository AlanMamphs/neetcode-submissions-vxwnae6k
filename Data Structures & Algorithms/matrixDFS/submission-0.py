class Solution:

    def dfs(self, grid, r, c, visited):
        ROWS, COLS = len(grid), len(grid[0])

        # Out of bounds
        if min(r, c) < 0 or r == ROWS or c == COLS:
            return 0

        # visited node
        if (r, c) in visited:
            return 0

        # Wall
        if grid[r][c] == 1:
            return 0

        # End Goal
        if r == ROWS - 1 and c == COLS - 1:
            return 1
        
        visited.add((r, c))

        count = 0
        # Left
        count += self.dfs(grid, r, c - 1, visited)
        # Top
        count += self.dfs(grid, r - 1, c, visited)
        # Right
        count += self.dfs(grid, r, c + 1, visited)
        # Bot
        count += self.dfs(grid, r + 1, c, visited)

        visited.remove((r, c))

        return count
        
    def countPaths(self, grid: List[List[int]]) -> int:
        visited = set()
        return self.dfs(grid, 0, 0, visited)