class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        R = len(text1)
        C = len(text2)
        
        dp = [0] * (C+1)
        for r in range(R - 1, -1, -1):
            temp = [0] * (C+1)
            for c in range(C - 1, -1, -1):
                res = 0
                if text1[r] == text2[c]:
                    res = 1 + dp[c+1]
                else:
                    res = max(dp[c], temp[c+1])
                temp[c] = res
            dp = temp
        return dp[0]
