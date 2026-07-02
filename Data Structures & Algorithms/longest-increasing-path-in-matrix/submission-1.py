class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = defaultdict(int)
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        R = len(matrix)
        C = len(matrix[0])
        def dfs(r, c, prev):
            if r not in range(R) or c not in range(C) or prev >= matrix[r][c]:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]
            
            res = 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                res = max(res, 1 + dfs(nr, nc, matrix[r][c]))
            
            cache[(r, c)] = res
            return res
        res = 0
        for i in range(R):
            for j in range(C):
                res = max(res, dfs(i, j, -1))
        return res