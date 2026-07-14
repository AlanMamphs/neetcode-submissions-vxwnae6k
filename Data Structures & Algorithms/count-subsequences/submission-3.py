class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = dict()

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if len(t) == j:
                return 1
            if len(s) == i:
                return 0
            # skip
            res = dfs(i + 1, j)
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            dp[(i, j)] = res
            return res
        
        return dfs(0,0 )