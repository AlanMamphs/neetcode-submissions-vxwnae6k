class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            n, m = m, n
        dp = [1] * n
        for i in range(m - 2, -1, -1):
            ndp = [1] * n
            for j in range(n - 2, -1, -1):
                ndp[j] = ndp[j + 1] + dp[j]
            dp = ndp
        return dp[0]
