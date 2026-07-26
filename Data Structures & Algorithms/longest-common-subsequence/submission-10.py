class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        R = len(text1)
        C = len(text2)
        dp = [0] * (C + 1)
        for r in range(R - 1, -1, -1):
            ndp = [0] * (C + 1)
            for c in range(C -1, -1, -1):
                if text1[r] == text2[c]:
                    ndp[c] = 1 + dp[c + 1]
                else:
                    ndp[c] = max(ndp[c + 1], dp[c])
            dp = ndp
        return dp[0]