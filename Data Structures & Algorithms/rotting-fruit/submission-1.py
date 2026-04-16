from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        visited = set()
        q = deque()
        count = 0
        for r in range(R):
            for c in range(C):
                v = grid[r][c]
                if v == 1:
                    count += 1
                elif v == 2:
                    q.append((r, c))
                    visited.add((r, c))
        print(count)
        if not count:
            return 0
        minutes = -1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    r1, c1 = r + dr, c + dc

                    if r1 not in range(R) or c1 not in range(C) or (r1, c1) in visited or grid[r1][c1] == 0:
                        continue
                    q.append((r1, c1))
                    visited.add((r1, c1))
                    count -= 1

            minutes += 1
        return minutes if not count else -1