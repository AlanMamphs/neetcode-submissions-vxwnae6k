class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        R = len(s)
        C = len(p)

        dp = [False] * (C + 1)
        dp[C] = True
        for r in range(R, -1, -1):
            ndp = [False] * (C + 1)
            ndp[C] = r == R
            for c in range(C, -1, -1):
                match = r < R and c < C and p[c] in ('.', s[r])
                if (c + 1) < C and p[c + 1] == '*':
                    ndp[c] = ndp[c + 2] or (match and (r < R and dp[c]))
                elif match:
                    ndp[c] = dp[c + 1]
            dp = ndp
        return dp[0]
        