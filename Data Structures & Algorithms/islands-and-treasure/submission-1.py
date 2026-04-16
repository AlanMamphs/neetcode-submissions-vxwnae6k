from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
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
            print(q, grid)
            for _ in range(len(q)):
                r, c, v = q.popleft()
                grid[r][c] = v

                for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    r1, c1 = r + dr, c + dc
                    if r1 not in range(R) or c1 not in range(C) or grid[r1][c1] == -1 or (r1, c1) in visited:
                        continue
                    visited.add((r1, c1))
                    q.append((r1, c1, v + 1))

        
