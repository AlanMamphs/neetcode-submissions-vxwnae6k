class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * (n)
        dp[-1] = 1

        for r in range(m - 1, -1, -1):
            ndp = [0] * (n)
            ndp[-1] = 1
            for c in range(n -2, -1, -1):
                ndp[c] = dp[c] + ndp[c + 1]
            dp = ndp
        return dp[0]