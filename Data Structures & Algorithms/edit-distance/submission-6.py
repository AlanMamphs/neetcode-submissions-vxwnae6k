class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        R = len(word1)
        C = len(word2)
        if R < C:
            R, C, word1, word2 = C, R, word2, word1
        dp = list(range(C, -1, -1))
        
        for r in range(R - 1, -1, -1):
            ndp = [0] * (C + 1)
            ndp[-1] = R - r
            for c in range(C -1, -1, -1):
                if word1[r] == word2[c]:
                    ndp[c] = dp[c + 1]
                else:
                    delete = dp[c]
                    insert = ndp[c + 1]
                    replace = dp[c + 1]

                    ndp[c] = 1 + min(delete, insert, replace)
            dp = ndp
        
        return dp[0]