class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        R = len(heights)
        C = len(heights[0])

        def dfs(r, c, local_max, visited):
            if r not in range(R) or c not in range(C):
                return
            
            if (r, c) in visited or heights[r][c] < local_max:
                return
            
            visited.add((r, c))
            local_max = heights[r][c]
            
            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                dfs(r + dr, c + dc, local_max, visited)
        
        for r in range(R):
            dfs(r, 0, -1, pacific)
            dfs(r, C - 1, -1, atlantic)


        for c in range(C):
            dfs(0, c, -1, pacific)
            dfs(R - 1, c, -1, atlantic)
        return list(pacific.intersection(atlantic))
