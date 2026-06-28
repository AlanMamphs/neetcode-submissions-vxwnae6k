class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1] * n
        for i in range(m - 1):
            curr = [1] * n
            for j in range(n - 2, -1, -1):
                curr[j] = prev[j] + curr[j + 1]
            prev = curr
        return prev[0]
            