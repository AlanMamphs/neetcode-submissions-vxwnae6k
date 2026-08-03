class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if (len(s1) + len(s2)) != len(s3):
            return False
        R = len(s1)
        C = len(s2)

        dp = [[False] * (C+1) for _ in range(R + 1)]
        dp[R][C] = True
        
        for r in range(R,-1,-1):
            for c in range(C, -1, -1):
                if r < R and s1[r] == s3[r+c]:
                    dp[r][c] = dp[r+1][c]
                if c < C and s2[c] == s3[r+c]:
                    dp[r][c] = dp[r][c+1]
            
        return dp[0][0]



