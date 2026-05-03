class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        R = len(heights)
        C = len(heights[0])

        def dfs(r, c, prev, visited):
            if r not in range(R) or c not in range(C) or (r, c) in visited or prev > heights[r][c]:
                return
            
            visited.add((r, c))
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                dfs(r + dr, c + dc, max(prev, heights[r][c]), visited)
        
        for r in range(R):
            dfs(r, 0, 0, pacific)
            dfs(r, C - 1, 0, atlantic)
        
        for c in range(C):
            dfs(0, c, 0, pacific)
            dfs(R - 1, c, 0, atlantic)
        
        return list(atlantic.intersection(pacific))
