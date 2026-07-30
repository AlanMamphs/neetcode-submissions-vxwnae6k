class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        R = len(word1)
        C = len(word2)

        dp = [[0] * (C + 1) for _ in range(R + 1)]
        dp[R][C] = 0

        for r in range(R):
            dp[r][C] = R - r
        
        for c in range(C):
            dp[R][c] = C - c
        
        for r in range(R - 1, -1, -1):
            for c in range(C -1, -1, -1):
                if word1[r] == word2[c]:
                    dp[r][c] = dp[r + 1][c + 1]
                else:
                    delete = dp[r + 1][c]
                    insert = dp[r][c + 1]
                    replace = dp[r + 1][c + 1]

                    dp[r][c] = 1 + min(delete, insert, replace)
        
        return dp[0][0]