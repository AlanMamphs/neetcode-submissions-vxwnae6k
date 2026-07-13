class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R = len(matrix)
        C = len(matrix[0])

        cache = dict()

        def dfs(r, c):
            if (r, c) in cache:
                return cache[(r, c)]
            res = 1
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if nr in range(R) and nc in range(C) and matrix[r][c] < matrix[nr][nc]:
                    res = max(res, 1 + dfs(nr, nc))
            cache[(r, c)] = res
            return res
        
        res = 0
        
        for i in range(R):
            for j in range(C):
                res = max(res, dfs(i, j))
        
        return res