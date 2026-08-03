class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        R = len(s)
        C = len(t)
        dp = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R + 1):
            dp[r][C] = 1
        for r in range(R - 1, -1, -1):
            for c in range(C - 1, -1, -1):
                dp[r][c] = dp[r + 1][c]
                if s[r] == t[c]:
                    dp[r][c] += dp[r + 1][c + 1]
        return dp[0][0]