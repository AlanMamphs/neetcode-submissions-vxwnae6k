class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        R = len(s)
        C = len(t)
        cache = dict()
        def dfs(r, c):
            if (r, c) in cache:
                return cache[(r, c)]
            if r == R or c == C:
                return int(c == C)
            
            res = dfs(r + 1, c)
            if s[r] == t[c]:
                res += dfs(r + 1, c + 1)
            cache[(r, c)] = res
            return res
        
        return dfs(0, 0)
            