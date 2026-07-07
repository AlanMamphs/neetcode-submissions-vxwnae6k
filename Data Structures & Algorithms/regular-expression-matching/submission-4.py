class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = dict()

        def dfs(i, j):
            if j == len(p):
                return i == len(s)
            if (i, j) in cache:
                return cache[(i, j)]
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            res = False
            
            if (j + 1) < len(p) and p[j + 1] == '*':
                res = dfs(i, j + 2) or (match and dfs(i + 1, j))
            elif match:
                res = dfs(i + 1, j + 1)
               
            cache[(i, j)] = res
            return res
        
        return dfs(0, 0)