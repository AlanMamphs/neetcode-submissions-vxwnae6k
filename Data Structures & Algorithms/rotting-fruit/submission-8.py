class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        R = len(grid)
        C = len(grid[0])
        count = 0
        visited = set()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    count += 1
        minute = 0
        while q:
            temp = []
            for r, c in q:
                for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    r2 = r + dr
                    c2 = c + dc
                    if r2 not in range(R) or c2 not in range(C) or grid[r2][c2] != 1:
                        continue
                    grid[r2][c2] = 2
                    temp.append((r2, c2))
            if temp:
                count -= len(temp)
                minute += 1
            q = temp
        print(count)
        return minute if count == 0 else -1