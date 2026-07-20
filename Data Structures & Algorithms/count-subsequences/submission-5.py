class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        C = len(t)
        R = len(s)
        dp = [0] * (C + 1)
        dp[C] = 1

        for r in range(R - 1, -1, -1):
            ndp = [0] * (C + 1)
            ndp[C] = 1
            for c in range(C - 1, -1, -1):
                ndp[c] = dp[c]
                if s[r] == t[c]:
                    ndp[c] += dp[c + 1]
            dp = ndp
        
        return dp[0]