class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        R = len(s1)
        C = len(s2)
        if R + C != len(s3):
            return False
        dp = [False] * (C + 1)
        dp[C] = 1

        for r in range(R, -1, -1):
            ndp = [False] * (C + 1)
            if r == R:
                ndp[C] = True
            for c in range(C, -1, -1):
                if r < R and s1[r] == s3[r + c]:
                    ndp[c] = dp[c]
                if c < C and s2[c] == s3[r + c]:
                    ndp[c] = ndp[c + 1]
            dp = ndp
        return dp[0]