from collections import deque

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        visited.add((0, 0))
        queue.append((0, 0))
        level = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if (row, col) == (ROWS - 1, COLS - 1):
                    return level
                for dr, dc in DIRS:
                    r, c = row + dr, col + dc

                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == 0 and (r, c) not in visited:
                        visited.add((r, c))
                        queue.append((r, c))
            
            level += 1
        return -1 
