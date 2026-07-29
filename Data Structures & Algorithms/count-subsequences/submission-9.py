class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        R = len(s)
        C = len(t)
        dp = [list([0] * (C + 1)) for _ in range(R + 1)]
        dp[R][C] = 1
        for r in range(R - 1, -1, -1):
            dp[r][C] = 1
            for c in range(C - 1, -1, -1):
                res = dp[r + 1][c]
                if s[r] == t[c]:
                    res += dp[r + 1][c + 1]
                dp[r][c] = res
            print(dp)
        return dp[0][0]
            