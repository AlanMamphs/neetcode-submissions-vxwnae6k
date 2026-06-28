class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1] * (m)
        for i in range(n - 1):
            curr = [1] * m
            for j in range(1, m):
                curr[j] = curr[j - 1] + prev[j]
            prev = curr
        return prev[-1]
