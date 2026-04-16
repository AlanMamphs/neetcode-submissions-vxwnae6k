class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R = len(heights)
        C = len(heights[0])
        res = []
        atlantic, pacific = set(), set()

        def dfs(r, c, visited, prev):
            if r not in range(R) or c not in range(C) or (r, c) in visited or heights[r][c] < prev:
                return

            visited.add((r, c))
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                dfs(r + dr, c + dc, visited, heights[r][c])

        
        for r in range(R):
            dfs(r, 0, pacific, float('-inf'))
            dfs(r, C - 1, atlantic, float('-inf'))

        for c in range(C):
            dfs(0, c, pacific, float('-inf'))
            dfs(R - 1, c, atlantic, float('-inf'))

        for r in range(R):
            for c in range(C):
                if (r, c) in atlantic and (r, c) in pacific:
                    res.append((r, c))
        return res