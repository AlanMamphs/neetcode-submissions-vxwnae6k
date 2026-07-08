class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0]*(m+1)
        curr = [0]*(m+1)
        prev[-2] = 1

        for i in range(n-1, -1,-1):
            for j in range(m-1, -1, -1):
                curr[j] = curr[j + 1] + prev[j]
            prev = curr
        
        return prev[0]