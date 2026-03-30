DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()
        max_area = 0

        def bfs(r, c):
            queue = collections.deque()
            visited.add((r, c))
            queue.append((r, c))
            area = 1
            while queue:
                row, col = queue.popleft()
                for dr, dc in DIRS:
                    r, c = row + dr, col + dc

                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == 1 and not (r, c) in visited:
                        area += 1
                        visited.add((r, c))
                        queue.append((r, c))

            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = bfs(r, c)
                    max_area = max(max_area, area)
        
        return max_area

