class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        R = len(s)
        C = len(p)
        dp = [False] * (C + 1)
        dp[C] = True

        for r in range(R, -1, -1):
            ndp = [False] * (C + 1)
            ndp[C] = r == R

            for c in range(C - 1, -1, -1):
                match = (r < R) and p[c] in (s[r], '.')
                res = False
                if (c + 1 < C) and p[c + 1] == '*':
                    # skip pattern
                    res = ndp[c + 2] or (match and dp[c])
                elif match:
                    res = dp[c + 1]
                ndp[c] = res
            dp = ndp
        
        return dp[0]