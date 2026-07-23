class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = dict()
        R = len(matrix)
        C = len(matrix[0])

        def dfs(r, c, prev):
            if (r, c, prev) in cache:
                return cache[(r, c, prev)]
            
            if r not in range(R) or c not in range(C):
                return 0
            
            if matrix[r][c] <= prev:
                return 0
            res = 1
            for dr, dc in ( (1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = dr + r, dc + c
                res = max(res, 1 + dfs(nr, nc, matrix[r][c]))
            
            cache[(r, c, prev)] = res
            return res
        
        res = 0
        for r in range(R):
            for c in range(C):
                res = max(dfs(r, c, float('-inf')), res)
        return res                